# -*- coding: utf-8 -*-
from django.db import models
# from ast import literal_eval


class NameListSZRepertory(models.Model):
    """
    suzhou base
    """
    nlr01 = models.CharField(max_length=32)
    nlr02 = models.CharField(max_length=32)


class NameListJJRepertory(models.Model):
    """
    jiujiang base
    """
    nlj01 = models.CharField(max_length=32)
    nlj02 = models.CharField(max_length=32)


class NameListCSRepertory(models.Model):
    """
    changshu base
    """
    nlsc01 = models.CharField(max_length=32)
    nlsc02 = models.CharField(max_length=32)


class MerchantJJ1Repertory(models.Model):
    """
    jj pailameng
    """
    mj101 = models.CharField(max_length=32)
    mj102 = models.CharField(max_length=32)


class MerchantJJ1RepertoryExtend(models.Model):
    STATUS_CHOICES = (
        (1, u'未处理'),
        (2, u'暂存'),
        (3, u'预约'),
    )
    # mjj1r = models.ForeignKey(MerchantJJ1Repertory, to_field=id)
    operator = models.CharField(verbose_name=u'操作者', max_length=64, default='')
    # operator field save who distribute this namelist
    salesman = models.CharField(verbose_name=u'业务员', max_length=64, default='')
    # salesman field save distribute namelist to which account
    is_enable = models.BooleanField(verbose_name=u'是否有效', default=True)
    # when call back this namelist, is_enable=False
    is_assigned = models.BooleanField(verbose_name=u'是否分配', default=False)
    status = models.CharField(verbose_name=u'处理状态', max_length=2, default='1',
                              choices=STATUS_CHOICES)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True, null=True)


class MerchantJJ2Repertory(models.Model):
    """
    jj renbao
    """
    mj201 = models.CharField(max_length=32)
    mj202 = models.CharField(max_length=32)
    operator = models.CharField(verbose_name=u'操作者', max_length=64, default='')
    # operator field save who distribute this namelist
    salesman = models.CharField(verbose_name=u'业务员', max_length=64, default='')
    # salesman field save distribute namelist to which account
    is_enable = models.BooleanField(verbose_name=u'是否有效', default=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True, null=True)


class MechantJJ3Repertory(models.Model):
    """
    jj tian'an
    """
    mj301 = models.CharField(max_length=32)
    mj302 = models.CharField(max_length=32)
    operator = models.CharField(verbose_name=u'操作者', max_length=64, default='')
    # operator field save who distribute this namelist
    salesman = models.CharField(verbose_name=u'业务员', max_length=64, default='')
    # salesman field save distribute namelist to which account
    is_enable = models.BooleanField(verbose_name=u'是否有效', default=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True, null=True)


class MerchantSZ1Repertory(models.Model):
    """
    sz team
    """
    msz101 = models.CharField(max_length=32)
    msz102 = models.CharField(max_length=32)
    operator = models.CharField(verbose_name=u'操作者', max_length=64, default='')
    # operator field save who distribute this namelist
    salesman = models.CharField(verbose_name=u'业务员', max_length=64, default='')
    # salesman field save distribute namelist to which account
    is_enable = models.BooleanField(verbose_name=u'是否有效', default=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True, null=True)


class MerchantSD1Repertory(models.Model):
    """
    sd team
    """
    msd101 = models.CharField(max_length=32)
    msd102 = models.CharField(max_length=32)
    operator = models.CharField(verbose_name=u'操作者', max_length=64, default='')
    # operator field save who distribute this namelist
    salesman = models.CharField(verbose_name=u'业务员', max_length=64, default='')
    # salesman field save distribute namelist to which account
    is_enable = models.BooleanField(verbose_name=u'是否有效', default=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True, null=True)


class NameListAssignToMerchantRecord(models.Model):
    """
    when assign namelist from NameListXXXRepertory to some merchant repertory
    record the distribution info;
    """
    dr01 = models.CharField(max_length=32)  # recode license_no
    dr02 = models.CharField(max_length=255)  # save name list divide to which merchant
    operator = models.CharField(verbose_name=u'操作者', max_length=64, default='')
    # save who distribute this namelist
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)


class NameListAssignToAccountRecord(models.Model):
    """
    when assign namelist from MerchantXXXRepertory to some account
    record the distribution info;
    """
    dr01 = models.CharField(max_length=32)  # recode license_no
    dr02 = models.CharField(max_length=255)  # save name list divide to which account
    operator = models.CharField(verbose_name=u'操作者', max_length=64, default='')
    # save who distribute this namelist
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)