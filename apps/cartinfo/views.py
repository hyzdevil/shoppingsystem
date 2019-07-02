import datetime
from django.shortcuts import render, redirect
from cartinfo.models import *
from userinfo.models import *
from commodityinfo.models import *
from django.http import JsonResponse

# Create your views here.

def add_cart(request):
    if request.session.get('is_login', None):
        user_id = request.session.get('user_id')
        good_id = request.POST.get('goods_id')
        ccount = request.POST.get('num')
        user = CartInfo.objects.filter(user_id=user_id,good_id=good_id)
        if user:
            user.ccount = int(user.ccount) + int(ccount)
            user.save()
        else:
            CartInfo.objects.create(user_id=user_id, good_id=good_id, ccount=ccount)
        message = "成功添加到购物车！"
    else:
        message = "您还没有登陆，请登陆..."
    return JsonResponse({"message":message})

def cart_info(request):
    all_rows = CartInfo.objects.all()  # 获取所有购物车数据
    all_goods = []
    for each_row in all_rows:
        # 查找出属于当前登录用户的购物车数据
        if each_row.user_id == request.session.get('user_id'):
            goods = Goods.objects.get(id=each_row.good_id)
            all_goods.append((goods, each_row.ccount, goods.price*each_row.ccount))
    if len(all_goods) == 0:
        msg = "您的购物车还是空的，快去购买吧..."
    else:
        msg = ""
    return render(request, 'cartinfo/cart.html', {"all_goods":all_goods,"meaasge":msg})

def delete_goods(request, each_goods_id):
    user_id = request.session.get('user_id')
    CartInfo.objects.filter(user_id=user_id, good_id=each_goods_id).delete()
    return redirect("cartinfo:cart_info")

def order(request):
    # 获取当前登录用户的id
    user_id = request.session.get('user_id')
    # 查询出当前登录用户的所有订单
    all_order = Order.objects.filter(user_id=user_id)
    if all_order:
        order_list = []
        for each_row in all_order:
            goods = Goods.objects.get(id=each_row.goods_id)
            order_list.append((goods, each_row))
        content = {"order":order_list}
        return render(request,'cartinfo/order.html',content)
    else:
        message = "您还没有订单"
        return render(request,'cartinfo/order.html',{"message":message})

def add_order(request):
    user_id = request.session.get('user_id')
    goods = request.POST.getlist('goods')
    for goods_list in goods:
        goods_list = goods_list.split(',')
        goods = Goods.objects.get(id=goods_list[0])
        recipients = Address.objects.filter(user_id=user_id).latest('id')
        orderdetail = goods.title+goods.detail
        adsname = recipients.aname
        adsphone = recipients.phone
        ads = recipients.address
        orderNo = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Order.objects.create(order_no=orderNo,order_detail=orderdetail,address_name=adsname,
                             address_phone=adsphone,address=ads,acot=int(goods_list[1]),acount=int(goods_list[2]),user_id=user_id,goods_id=goods.id)
        CartInfo.objects.filter(user_id=user_id,good_id=goods_list[0]).delete()
    return JsonResponse({"message":"添加成功！"})

def place_order(request):
    # 判断用户是否登陆：LoginRequiredMixin
    sgoods = []
    total_count = 0
    total_goods_amount = 0
    if request.session.get('is_login', None):
        count = request.POST.get('num')
        if count is not None:  # 从直接购买进入确认订单界面
            goods_id = request.POST.get('goods_id')
            goods = Goods.objects.get(id=goods_id)
            amount = goods.price*int(count)
            sgoods.append((goods, int(count), amount))
            total_count += int(count)
            total_goods_amount += amount
        else:  # 从购物车进入确认订单界面
            user_id = request.session.get('user_id')
            goods_ids = request.POST.getlist('goods_ids')
            for goods_id in goods_ids:
                goods = Goods.objects.get(id=goods_id)
                goods_count = CartInfo.objects.get(user_id=user_id,good_id=goods.id).ccount
                goods_count = int(goods_count)
                amount = goods_count * goods.price
                sgoods.append((goods, goods_count, amount))
                total_count += goods_count
                total_goods_amount += amount
        try:
            address = Address.objects.filter(user_id=request.session.get('user_id')).latest('id')
        except Address.DoesNotExist:
            address = None
        context = {
            "goods" : sgoods,
            "total_count" : total_count,
            "total_goods_amount" : total_goods_amount,
            "address" : address
        }
        return render(request, 'cartinfo/placeorder.html', context)
    else:
        message = "您还没有登陆，请登陆..."
        return render(request, 'commodityinfo/commoditydetail.html', {"message":message})