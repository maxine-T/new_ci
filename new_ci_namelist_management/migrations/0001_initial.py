# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MerchantJJ1Repertory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_no', models.CharField(unique=True, max_length=64, verbose_name='\u8f66\u724c\u53f7')),
                ('car_brand', models.CharField(max_length=64, null=True, verbose_name='\u54c1\u724c', blank=True)),
                ('name', models.CharField(max_length=254, null=True, verbose_name='\u5ba2\u6237\u540d', blank=True)),
                ('tel', models.CharField(max_length=64, null=True, verbose_name='\u56fa\u5b9a\u7535\u8bdd', blank=True)),
                ('phone', models.CharField(max_length=64, null=True, verbose_name='\u624b\u673a\u53f7\u7801', blank=True)),
                ('address', models.CharField(max_length=254, null=True, verbose_name='\u8054\u7cfb\u5730\u5740', blank=True)),
                ('registered_time', models.DateField(null=True, verbose_name='\u767b\u8bb0\u65f6\u95f4', blank=True)),
                ('id_no', models.CharField(max_length=64, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7', blank=True)),
                ('car_brand_no', models.CharField(max_length=64, null=True, verbose_name='\u8f66\u578b\u53f7', blank=True)),
                ('vin_no', models.CharField(max_length=128, null=True, verbose_name='\u8f66\u67b6\u53f7', blank=True)),
                ('engine_no', models.CharField(max_length=64, null=True, verbose_name='\u53d1\u52a8\u673a\u53f7', blank=True)),
            ],
            options={
                'db_table': 'new_ci_merchant_jj1_rep',
            },
        ),
        migrations.CreateModel(
            name='MerchantJJ1RepertoryExtend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operator', models.CharField(default=b'', max_length=64, verbose_name='\u64cd\u4f5c\u8005')),
                ('salesman', models.CharField(default=b'', max_length=64, verbose_name='\u4e1a\u52a1\u5458')),
                ('is_enable', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('is_assigned', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5206\u914d')),
                ('info_status', models.CharField(default=b'A', max_length=2, verbose_name='\u4fe1\u606f\u72b6\u6001', choices=[(b'A', '\u672a\u5904\u7406'), (b'B', '\u6682\u5b58'), (b'C', '\u9884\u7ea6'), (b'D', '\u6210\u529f'), (b'E', '\u5931\u8d25'), (b'F', '\u65e0\u6548'), (b'G', '\u9700\u4fee\u6539')])),
                ('custom_type', models.CharField(default=b'A', max_length=2, verbose_name='\u5ba2\u6237\u7c7b\u578b', choices=[(b'N', b'\xe6\x97\xa0'), (b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E')])),
                ('appoint_time', models.DateTimeField(default=b'', verbose_name='\u9884\u7ea6\u65f6\u95f4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True)),
            ],
            options={
                'db_table': 'new_ci_merchant_jj1_rep_ext',
            },
        ),
        migrations.CreateModel(
            name='MerchantJJ2Repertory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_no', models.CharField(unique=True, max_length=64, verbose_name='\u8f66\u724c\u53f7')),
                ('car_brand', models.CharField(max_length=64, null=True, verbose_name='\u54c1\u724c', blank=True)),
                ('name', models.CharField(max_length=254, null=True, verbose_name='\u5ba2\u6237\u540d', blank=True)),
                ('tel', models.CharField(max_length=64, null=True, verbose_name='\u56fa\u5b9a\u7535\u8bdd', blank=True)),
                ('phone', models.CharField(max_length=64, null=True, verbose_name='\u624b\u673a\u53f7\u7801', blank=True)),
                ('address', models.CharField(max_length=254, null=True, verbose_name='\u8054\u7cfb\u5730\u5740', blank=True)),
                ('registered_time', models.DateField(null=True, verbose_name='\u767b\u8bb0\u65f6\u95f4', blank=True)),
                ('id_no', models.CharField(max_length=64, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7', blank=True)),
                ('car_brand_no', models.CharField(max_length=64, null=True, verbose_name='\u8f66\u578b\u53f7', blank=True)),
                ('vin_no', models.CharField(max_length=128, null=True, verbose_name='\u8f66\u67b6\u53f7', blank=True)),
                ('engine_no', models.CharField(max_length=64, null=True, verbose_name='\u53d1\u52a8\u673a\u53f7', blank=True)),
            ],
            options={
                'db_table': 'new_ci_merchant_jj2_rep',
            },
        ),
        migrations.CreateModel(
            name='MerchantJJ3Repertory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_no', models.CharField(unique=True, max_length=64, verbose_name='\u8f66\u724c\u53f7')),
                ('car_brand', models.CharField(max_length=64, null=True, verbose_name='\u54c1\u724c', blank=True)),
                ('name', models.CharField(max_length=254, null=True, verbose_name='\u5ba2\u6237\u540d', blank=True)),
                ('tel', models.CharField(max_length=64, null=True, verbose_name='\u56fa\u5b9a\u7535\u8bdd', blank=True)),
                ('phone', models.CharField(max_length=64, null=True, verbose_name='\u624b\u673a\u53f7\u7801', blank=True)),
                ('address', models.CharField(max_length=254, null=True, verbose_name='\u8054\u7cfb\u5730\u5740', blank=True)),
                ('registered_time', models.DateField(null=True, verbose_name='\u767b\u8bb0\u65f6\u95f4', blank=True)),
                ('id_no', models.CharField(max_length=64, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7', blank=True)),
                ('car_brand_no', models.CharField(max_length=64, null=True, verbose_name='\u8f66\u578b\u53f7', blank=True)),
                ('vin_no', models.CharField(max_length=128, null=True, verbose_name='\u8f66\u67b6\u53f7', blank=True)),
                ('engine_no', models.CharField(max_length=64, null=True, verbose_name='\u53d1\u52a8\u673a\u53f7', blank=True)),
            ],
            options={
                'db_table': 'new_ci_merchant_jj3_rep',
            },
        ),
        migrations.CreateModel(
            name='MerchantSD1Repertory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_no', models.CharField(unique=True, max_length=64, verbose_name='\u8f66\u724c\u53f7')),
                ('car_brand', models.CharField(max_length=64, null=True, verbose_name='\u54c1\u724c', blank=True)),
                ('name', models.CharField(max_length=254, null=True, verbose_name='\u5ba2\u6237\u540d', blank=True)),
                ('tel', models.CharField(max_length=64, null=True, verbose_name='\u56fa\u5b9a\u7535\u8bdd', blank=True)),
                ('phone', models.CharField(max_length=64, null=True, verbose_name='\u624b\u673a\u53f7\u7801', blank=True)),
                ('address', models.CharField(max_length=254, null=True, verbose_name='\u8054\u7cfb\u5730\u5740', blank=True)),
                ('registered_time', models.DateField(null=True, verbose_name='\u767b\u8bb0\u65f6\u95f4', blank=True)),
                ('id_no', models.CharField(max_length=64, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7', blank=True)),
                ('car_brand_no', models.CharField(max_length=64, null=True, verbose_name='\u8f66\u578b\u53f7', blank=True)),
                ('vin_no', models.CharField(max_length=128, null=True, verbose_name='\u8f66\u67b6\u53f7', blank=True)),
                ('engine_no', models.CharField(max_length=64, null=True, verbose_name='\u53d1\u52a8\u673a\u53f7', blank=True)),
            ],
            options={
                'db_table': 'new_ci_merchant_sd1_rep',
            },
        ),
        migrations.CreateModel(
            name='MerchantSZ1Repertory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_no', models.CharField(unique=True, max_length=64, verbose_name='\u8f66\u724c\u53f7')),
                ('car_brand', models.CharField(max_length=64, null=True, verbose_name='\u54c1\u724c', blank=True)),
                ('name', models.CharField(max_length=254, null=True, verbose_name='\u5ba2\u6237\u540d', blank=True)),
                ('tel', models.CharField(max_length=64, null=True, verbose_name='\u56fa\u5b9a\u7535\u8bdd', blank=True)),
                ('phone', models.CharField(max_length=64, null=True, verbose_name='\u624b\u673a\u53f7\u7801', blank=True)),
                ('address', models.CharField(max_length=254, null=True, verbose_name='\u8054\u7cfb\u5730\u5740', blank=True)),
                ('registered_time', models.DateField(null=True, verbose_name='\u767b\u8bb0\u65f6\u95f4', blank=True)),
                ('id_no', models.CharField(max_length=64, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7', blank=True)),
                ('car_brand_no', models.CharField(max_length=64, null=True, verbose_name='\u8f66\u578b\u53f7', blank=True)),
                ('vin_no', models.CharField(max_length=128, null=True, verbose_name='\u8f66\u67b6\u53f7', blank=True)),
                ('engine_no', models.CharField(max_length=64, null=True, verbose_name='\u53d1\u52a8\u673a\u53f7', blank=True)),
            ],
            options={
                'db_table': 'new_ci_merchant_sz1_rep',
            },
        ),
        migrations.CreateModel(
            name='NameListAssignToAccountRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('repertory_name', models.CharField(max_length=64)),
                ('nl_id', models.CharField(max_length=16)),
                ('license_no', models.CharField(max_length=64)),
                ('account_id', models.CharField(max_length=64)),
                ('operator', models.CharField(default=b'', max_length=64, verbose_name='\u64cd\u4f5c\u8005')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'db_table': 'new_ci_nl_to_account_record',
            },
        ),
        migrations.CreateModel(
            name='NameListAssignToMerchantRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('repertory_name', models.CharField(max_length=64)),
                ('nl_id', models.CharField(max_length=16)),
                ('license_no', models.CharField(max_length=64)),
                ('merchant_name', models.CharField(max_length=64)),
                ('operator', models.CharField(default=b'', max_length=64, verbose_name='\u64cd\u4f5c\u8005')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'db_table': 'new_ci_nl_to_merchant_record',
            },
        ),
        migrations.CreateModel(
            name='NameListCSRepertory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_no', models.CharField(unique=True, max_length=64, verbose_name='\u8f66\u724c\u53f7')),
                ('car_brand', models.CharField(max_length=64, null=True, verbose_name='\u54c1\u724c', blank=True)),
                ('name', models.CharField(max_length=254, null=True, verbose_name='\u5ba2\u6237\u540d', blank=True)),
                ('tel', models.CharField(max_length=64, null=True, verbose_name='\u56fa\u5b9a\u7535\u8bdd', blank=True)),
                ('phone', models.CharField(max_length=64, null=True, verbose_name='\u624b\u673a\u53f7\u7801', blank=True)),
                ('address', models.CharField(max_length=254, null=True, verbose_name='\u8054\u7cfb\u5730\u5740', blank=True)),
                ('registered_time', models.DateField(null=True, verbose_name='\u767b\u8bb0\u65f6\u95f4', blank=True)),
                ('id_no', models.CharField(max_length=64, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7', blank=True)),
                ('car_brand_no', models.CharField(max_length=64, null=True, verbose_name='\u8f66\u578b\u53f7', blank=True)),
                ('vin_no', models.CharField(max_length=128, null=True, verbose_name='\u8f66\u67b6\u53f7', blank=True)),
                ('engine_no', models.CharField(max_length=64, null=True, verbose_name='\u53d1\u52a8\u673a\u53f7', blank=True)),
            ],
            options={
                'db_table': 'new_ci_nl_cs_rep',
            },
        ),
        migrations.CreateModel(
            name='NameListJJRepertory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_no', models.CharField(unique=True, max_length=64, verbose_name='\u8f66\u724c\u53f7')),
                ('car_brand', models.CharField(max_length=64, null=True, verbose_name='\u54c1\u724c', blank=True)),
                ('name', models.CharField(max_length=254, null=True, verbose_name='\u5ba2\u6237\u540d', blank=True)),
                ('tel', models.CharField(max_length=64, null=True, verbose_name='\u56fa\u5b9a\u7535\u8bdd', blank=True)),
                ('phone', models.CharField(max_length=64, null=True, verbose_name='\u624b\u673a\u53f7\u7801', blank=True)),
                ('address', models.CharField(max_length=254, null=True, verbose_name='\u8054\u7cfb\u5730\u5740', blank=True)),
                ('registered_time', models.DateField(null=True, verbose_name='\u767b\u8bb0\u65f6\u95f4', blank=True)),
                ('id_no', models.CharField(max_length=64, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7', blank=True)),
                ('car_brand_no', models.CharField(max_length=64, null=True, verbose_name='\u8f66\u578b\u53f7', blank=True)),
                ('vin_no', models.CharField(max_length=128, null=True, verbose_name='\u8f66\u67b6\u53f7', blank=True)),
                ('engine_no', models.CharField(max_length=64, null=True, verbose_name='\u53d1\u52a8\u673a\u53f7', blank=True)),
            ],
            options={
                'db_table': 'new_ci_nl_jj_rep',
            },
        ),
        migrations.CreateModel(
            name='NameListSZRepertory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('license_no', models.CharField(unique=True, max_length=64, verbose_name='\u8f66\u724c\u53f7')),
                ('car_brand', models.CharField(max_length=64, null=True, verbose_name='\u54c1\u724c', blank=True)),
                ('name', models.CharField(max_length=254, null=True, verbose_name='\u5ba2\u6237\u540d', blank=True)),
                ('tel', models.CharField(max_length=64, null=True, verbose_name='\u56fa\u5b9a\u7535\u8bdd', blank=True)),
                ('phone', models.CharField(max_length=64, null=True, verbose_name='\u624b\u673a\u53f7\u7801', blank=True)),
                ('address', models.CharField(max_length=254, null=True, verbose_name='\u8054\u7cfb\u5730\u5740', blank=True)),
                ('registered_time', models.DateField(null=True, verbose_name='\u767b\u8bb0\u65f6\u95f4', blank=True)),
                ('id_no', models.CharField(max_length=64, null=True, verbose_name='\u8eab\u4efd\u8bc1\u53f7', blank=True)),
                ('car_brand_no', models.CharField(max_length=64, null=True, verbose_name='\u8f66\u578b\u53f7', blank=True)),
                ('vin_no', models.CharField(max_length=128, null=True, verbose_name='\u8f66\u67b6\u53f7', blank=True)),
                ('engine_no', models.CharField(max_length=64, null=True, verbose_name='\u53d1\u52a8\u673a\u53f7', blank=True)),
            ],
            options={
                'db_table': 'new_ci_nl_sz_rep',
            },
        ),
        migrations.AddField(
            model_name='merchantjj1repertory',
            name='mjj1r_ext',
            field=models.ForeignKey(related_name='mjj1r_info', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='new_ci_namelist_management.MerchantJJ1RepertoryExtend', null=True),
        ),
    ]
