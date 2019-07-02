from django.db import models

# Create your models here.

class GoodsType(models.Model):
    title = models.CharField('分类名称',max_length=30)
    isdelete = models.BooleanField('是否删除',default=False)

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = "商品类别"

    def __str__(self):
        return self.title

class Goods(models.Model):
    title = models.CharField('商品名称',max_length=30,null=False)
    price = models.DecimalField('价格',max_length=10,decimal_places=2,max_digits=10)
    picture = models.ImageField('商品图片',upload_to='category',default='normal.png')
    detail = models.TextField('商品详情',blank=True,default='商品详情')
    isdelete = models.BooleanField('是否删除',default=False)
    type = models.ForeignKey(GoodsType,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"

    def __str__(self):
        return self.title