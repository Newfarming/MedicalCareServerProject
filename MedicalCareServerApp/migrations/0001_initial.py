# Generated by Django 4.0.5 on 2022-06-21 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=255, verbose_name='app_label')),
                ('api', models.CharField(max_length=255, verbose_name='api借口')),
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
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='权限名称')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicalCareServerApp.contenttype', verbose_name='权限类型')),
            ],
        ),
    ]
