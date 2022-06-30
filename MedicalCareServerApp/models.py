from django.db import models


# Create your models here.
class Department(models.Model):
    # 部门表
    title = models.CharField(verbose_name="部门名称", max_length=32)

    def __str__(self):
        # 解决ModelForm的外键引用返回对象的问题.
        return self.title


# 权限说明 1:用户新增 '/user/add' 2:用户删除 '/user/delete' 3:用户查找 '/user/list' '/user/details' 4:用户修改 '/user/edit' 5:部门新增
# '/depart/add' 6:部门删除 '/depart/delete' 7:部门查找 '/depart/list' '/depart/details' 8:部门修改 '/depart/edit' 9:活动新增
# '/activity/add' 10:活动删除 '/activity/delete' 11:活动查找 '/activity/list' '/activity/details' 12:活动修改 '/activity/edit'
class Permission(models.Model):
    # 权限表
    name = models.CharField(verbose_name="权限名称", max_length=255)
    content_type = models.CharField(verbose_name="权限内容", max_length=255, default="")

    def __str__(self):
        return self.name


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
    permission = models.ForeignKey(verbose_name="部门", to="Permission", to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class ActivityInfo(models.Model):
    """活动"""
    name = models.CharField(verbose_name="活动名", max_length=64)
    place = models.CharField(verbose_name="地点", max_length=64)
    start_time = models.DateField(verbose_name="活动开始时间")
    lasting_time = models.CharField(verbose_name="持续时间", max_length=64)
    score = models.CharField(verbose_name="积分", max_length=64)
    status_choices = (
        (0, "未开始"),
        (1, "进行中"),
        (2, "已结束"),
    )
    activity_status = models.SmallIntegerField(verbose_name="活动状态", choices=status_choices)

    def __str__(self):
        return self.name

