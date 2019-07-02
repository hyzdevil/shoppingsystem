from django.db import models

# Create your models here.


class UserInfo(models.Model):
    uname = models.CharField('用户名',max_length=50,null=False)
    upassword = models.CharField('密码',max_length=200,null=False)
    email = models.CharField('邮箱',max_length=50)
    phone = models.CharField('手机',max_length=20,null=False,unique=True)
    time = models.DateTimeField('注册时间',auto_now_add=True)
    isban = models.BooleanField('是否禁用',default=False)
    isdelete = models.BooleanField('是否删除',default=False)
    USERNAME_FIELD = 'uname'
    def __str__(self):
        return self.uname

class Address(models.Model):
    aname = models.CharField('收货人',max_length=50,null=False)
    address = models.CharField('收获地址',max_length=300,null=False)
    phone = models.CharField('电话',max_length=20,null=False)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.aname

class AreanInfo(models.Model):
    atitle = models.CharField(max_length=30)
    aparent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.atitle