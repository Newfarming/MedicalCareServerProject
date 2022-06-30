# Generated by Django 4.0.3 on 2022-06-29 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='活动名')),
                ('place', models.CharField(max_length=64, verbose_name='地点')),
                ('start_time', models.DateField(verbose_name='活动开始时间')),
                ('lasting_time', models.CharField(max_length=64, verbose_name='持续时间')),
                ('score', models.CharField(max_length=64, verbose_name='积分')),
                ('activity_status', models.SmallIntegerField(choices=[(0, '未开始'), (1, '进行中'), (2, '已结束')], verbose_name='活动状态')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='部门名称')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='权限名称')),
                ('content_type', models.CharField(default='', max_length=255, verbose_name='权限内容')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('password', models.CharField(default='123456', max_length=64, verbose_name='密码')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('workNo', models.CharField(max_length=32, verbose_name='工号')),
                ('identityCard', models.CharField(max_length=64, verbose_name='身份证')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicalCareServerApp.department', verbose_name='部门')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicalCareServerApp.permission', verbose_name='部门')),
            ],
        ),
    ]
