from django.shortcuts import render, redirect
from userinfo.models import *
from userinfo.forms import UserForm, RegisterForm
import hashlib
from django.http import JsonResponse

# Create your views here.

def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

def register(request):
    if request.session.get('is_login', None):   # 判断用户是否登录
        return redirect('commodityinfo:index')
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # 获取注册信息
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            phone = register_form.cleaned_data['phone']
            # 对注册信息进行数据库比对
            if password1 != password2:
                message = "两次输入的密码不相同！"
                return render(request, 'userinfo/register.html', locals())
            else:
                same_name_user = UserInfo.objects.filter(uname=username)
                if same_name_user:
                    message = "该用户已存在！"
                    return render(request, 'userinfo/register.html', locals())
                same_email_user = UserInfo.objects.filter(email=email)
                if same_email_user:
                    message = "该邮箱已被注册！"
                    return render(request, 'userinfo/register.html', locals())
                same_phone_user = UserInfo.objects.filter(phone=phone)
                if same_phone_user:
                    message = "该手机已被注册！"
                    return render(request, 'userinfo/register.html', locals())
                # 将用户信息保存在数据库中并跳转到登录界面
                new_user = UserInfo.objects.create()
                new_user.uname = username
                new_user.upassword = hash_code(password1)
                new_user.email = email
                new_user.phone = phone
                new_user.save()
                return redirect('userinfo:login')
    register_form = RegisterForm()
    return render(request, 'userinfo/register.html', locals())

def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            # username = username.strip()
            try:
                user = UserInfo.objects.get(uname=username)
                if user.upassword == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.uname
                    request.session.set_expiry(0)
                    return redirect('commodityinfo:index')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'userinfo/login.html',locals())
    login_form = UserForm()
    return render(request, 'userinfo/login.html', locals())

def login_out(request):
    if not request.session.get('is_login', None):
        return redirect("commodityinfo:index")
    request.session.flush()
    return redirect('commodityinfo:index')

def personal(request):
    return render(request, 'userinfo/personal.html')

def user_address(request):
    user_site = Address.objects.filter(user_id=request.session.get('user_id'))
    site_list = []
    if user_site:
        message = ""
        for each_row in user_site:
            site_list.append((each_row.aname, each_row.address, each_row.phone))
    else:
        message = "您还没有收货地址..."
    return render(request, 'userinfo/myaddress.html', {"site_list":site_list,"message":message})

def delete_address(request):
    user_id = request.session.get('user_id')
    name = request.POST.get('recipients_name')
    address = request.POST.get('recipients_address')
    Address.objects.filter(user_id=user_id, aname=name, address=address).delete()
    return JsonResponse({"message":"删除成功！"})

def add_address(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        aname = request.POST.get('name')
        province = request.POST.get('province')
        city = request.POST.get('city')
        district = request.POST.get('district')
        detail = request.POST.get('detail')
        aphone = request.POST.get('phone')
        address = str(province)+str(city)+str(district)+str(detail)
        site = Address.objects.filter(aname=aname,address=address,phone=aphone,user_id=user_id)
        if site:
            message = "该地址已存在..."
        else:
            Address.objects.create(aname=aname,address=address,phone=aphone,user_id=user_id)
            message = "保存成功！"
        return JsonResponse({"message":message})
    return render(request, 'userinfo/add_site.html')

def getProvince(request):
    provinces = AreanInfo.objects.filter(aparent__isnull=True)
    res = []
    for i in provinces:
        res.append([i.id, i.atitle])
    return JsonResponse({"provinces":res})

def getCity(request):
    city_id = request.GET.get('city_id')
    cities = AreanInfo.objects.filter(aparent_id=city_id)
    res = []
    for i in cities:
        res.append([i.id, i.atitle])
    return JsonResponse({"cities":res})

def getDistrict(request):
    district_id = request.GET.get('district_id')
    cities = AreanInfo.objects.filter(aparent_id=district_id)
    res = []
    for i in cities:
        res.append([i.id, i.atitle])
    return JsonResponse({'district': res})

