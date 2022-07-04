# Generated by Django 4.0.3 on 2022-07-01 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MedicalCareServerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='superAdmin',
            field=models.CharField(default='0', max_length=64, verbose_name='超级管理员'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedicalCareServerApp.permission', verbose_name='权限'),
        ),
    ]