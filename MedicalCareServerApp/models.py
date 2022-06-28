from django.db import models


# Create your models here.
class Department(models.Model):
    # 部门表
    title = models.CharField(verbose_name="部门名称", max_length=32)

    def __str__(self):
        # 解决ModelForm的外键引用返回对象的问题.
        return self.title


class UserInfo(models.Model):
    """员工"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64, default="123456")
    phone = models.CharField(verbose_name="手机号", max_length=11)
    workNo = models.CharField(verbose_name="工号", max_length=32)
    identityCard = models.CharField(verbose_name="身份证", max_length=64)
    # 外键 自动生成的字段名为: depart_id,_id是django自动添加的
    # 如果 部门表被删除, 则级联删除
    depart = models.ForeignKey(verbose_name="部门", to="Department", to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Permission(models.Model):
    name = models.CharField(verbose_name="权限名称", max_length=255)
    content_type = models.CharField(verbose_name="权限内容", max_length=64, default="")
    # codename = models.CharField(verbose_name="codename", max_length=100)

    def __str__(self):
        return self.name


# class ContentType(models.Model):
#     app_label = models.CharField(verbose_name="app_label", max_length=255)
#     api = models.CharField(verbose_name="api接口", max_length=255)
#
#     def __str__(self):
#         return self.app_label


class ActivityInfo(models.Model):
    """活动"""
    name = models.CharField(verbose_name="活动名", max_length=64)
    place = models.CharField(verbose_name="地点", max_length=64)
    start_time = models.DateField(verbose_name="活动开始时间")
    lasting_time = models.CharField(verbose_name="持续时间", max_length=64)
    score = models.CharField(verbose_name="积分", max_length=64)
    status_choices = (
        (1, "未开始"),
        (2, "进行中"),
        (2, "已结束"),
    )
    activity_status = models.SmallIntegerField(verbose_name="活动状态", choices=status_choices)

    def __str__(self):
        return self.name

