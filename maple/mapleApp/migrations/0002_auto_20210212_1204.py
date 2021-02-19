# Generated by Django 3.1.5 on 2021-02-12 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapleApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('cash', '현금'), ('card', '카드')], max_length=20, verbose_name='결제구분'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('prep', '준비중'), ('done', '완료'), ('ord', '주문')], max_length=20, verbose_name='완료여부'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='jobtitle',
            field=models.CharField(choices=[('J50', '아르바이트'), ('J40', '인턴'), ('J10', 'CEO'), ('J30', '사원'), ('J20', '메니저')], max_length=20, verbose_name='직급'),
        ),
    ]
