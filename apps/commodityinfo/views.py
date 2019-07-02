from django.shortcuts import render,get_object_or_404
from commodityinfo.models import *

# Create your views here.

def index(request):
    all_type = GoodsType.objects.all()  # 获取所有的商品类型
    favorate_commodity = []
    cost_performance = []
    for each_type in all_type:
        favorate_commodity.append((each_type, Goods.objects.filter(type=each_type, isdelete=False)[:1]))
        cost_performance.append((each_type, Goods.objects.filter(type=each_type, isdelete=False)[1:2]))
    content = {"favorate_commodity":favorate_commodity,"cost_performance":cost_performance,"all_type":all_type}
    return render(request, 'commodityinfo/index.html', content)

def typedetail(request, each_type_id):
    all_type = GoodsType.objects.all()
    needtype = get_object_or_404(GoodsType, id=each_type_id)
    commodity = [(needtype, Goods.objects.filter(type=needtype ,isdelete=False))]
    content = {"type_commodity": commodity, "all_type": all_type}
    return render(request, 'commodityinfo/typedetail.html', content)

def commoditydetail(request, each_type_id, commodity_id):
    all_type = GoodsType.objects.all()
    commodity = get_object_or_404(Goods, id=commodity_id, isdelete=False)
    content = {'commodity':commodity, 'all_type':all_type}
    return render(request, 'commodityinfo/commoditydetail.html', content)