from django.db import models
from userinfo.models import UserInfo
from commodityinfo.models import Goods

# Create your models here.
# 购物车CartInfo
# id
# user 用户（关联UserInfo）
# goods 商品（关联Goods）
# ccount 数量（数量）

ORDERSTATUS = (
    (1,'未支付'),
    (2,'已支付'),
    (3,'订单取消'),
)

class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo,db_column='user_id',on_delete=models.CASCADE)
    good = models.ForeignKey(Goods,db_column='good_id',on_delete=models.CASCADE)
    ccount = models.IntegerField('数量',db_column='cart_count')

    def __str__(self):
        return self.user

# 订单表Order
# id
# orderNo 订单号
# orderDetail 详情（商品，数量，单价，描述）
# addressName 收件人
# addressPhone 收件人电话
# address 地址
# user 用户（关联）
# time 时间
# acot 总数
# acount 总价
# orderstatus 状态

class Order(models.Model):
    order_no = models.CharField('商品编号',max_length=50)
    order_detail = models.TextField('订单详情')
    address_name = models.CharField('收件人姓名',max_length=30,null=False)
    address_phone = models.CharField('收件人电话',max_length=20,null=False)
    address = models.CharField('地址',max_length=300)
    time = models.DateTimeField(auto_now_add=True)
    acot = models.IntegerField('总数')
    acount = models.DecimalField('总价',max_length=10,decimal_places=2,max_digits=10)
    order_status = models.IntegerField('订单',choices=ORDERSTATUS,default=1)
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_no