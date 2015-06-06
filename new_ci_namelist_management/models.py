# -*- coding: utf-8 -*-
from django.db import models
from util.setting import INFO_STATUS_CHOICES, CUSTOM_TYPE_CHOICES
# from ast import literal_eval


class NameListSZRepertory(models.Model):
    """
    suzhou base
    """
    license_no = models.CharField(unique=True, verbose_name=u"车牌号", max_length=64)
    car_brand = models.CharField(verbose_name=u"品牌", max_length=64, null=True, blank=True)
    name = models.CharField(verbose_name=u"客户名", max_length=254, null=True, blank=True)
    tel = models.CharField(verbose_name=u"固定电话", max_length=64, null=True, blank=True)
    phone = models.CharField(verbose_name=u"手机号码", max_length=64, null=True, blank=True)
    address = models.CharField(verbose_name=u"联系地址", max_length=254, null=True, blank=True)
    registered_time = models.DateField(verbose_name=u"登记时间", null=True, blank=True)
    id_no = models.CharField(verbose_name=u"身份证号", max_length=64, null=True, blank=True)
    car_brand_no = models.CharField(verbose_name=u"车型号", max_length=64, null=True, blank=True)
    vin_no = models.CharField(verbose_name=u"车架号", max_length=128, blank=True, null=True)
    engine_no = models.CharField(verbose_name=u"发动机号", max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'new_ci_nl_sz_rep'


class NameListJJRepertory(models.Model):
    """
    jiujiang base
    """
    license_no = models.CharField(unique=True, verbose_name=u"车牌号", max_length=64)
    car_brand = models.CharField(verbose_name=u"品牌", max_length=64, null=True, blank=True)
    name = models.CharField(verbose_name=u"客户名", max_length=254, null=True, blank=True)
    tel = models.CharField(verbose_name=u"固定电话", max_length=64, null=True, blank=True)
    phone = models.CharField(verbose_name=u"手机号码", max_length=64, null=True, blank=True)
    address = models.CharField(verbose_name=u"联系地址", max_length=254, null=True, blank=True)
    registered_time = models.DateField(verbose_name=u"登记时间", null=True, blank=True)
    id_no = models.CharField(verbose_name=u"身份证号", max_length=64, null=True, blank=True)
    car_brand_no = models.CharField(verbose_name=u"车型号", max_length=64, null=True, blank=True)
    vin_no = models.CharField(verbose_name=u"车架号", max_length=128, blank=True, null=True)
    engine_no = models.CharField(verbose_name=u"发动机号", max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'new_ci_nl_jj_rep'


class NameListCSRepertory(models.Model):
    """
    changshu base
    """
    license_no = models.CharField(unique=True, verbose_name=u"车牌号", max_length=64)
    car_brand = models.CharField(verbose_name=u"品牌", max_length=64, null=True, blank=True)
    name = models.CharField(verbose_name=u"客户名", max_length=254, null=True, blank=True)
    tel = models.CharField(verbose_name=u"固定电话", max_length=64, null=True, blank=True)
    phone = models.CharField(verbose_name=u"手机号码", max_length=64, null=True, blank=True)
    address = models.CharField(verbose_name=u"联系地址", max_length=254, null=True, blank=True)
    registered_time = models.DateField(verbose_name=u"登记时间", null=True, blank=True)
    id_no = models.CharField(verbose_name=u"身份证号", max_length=64, null=True, blank=True)
    car_brand_no = models.CharField(verbose_name=u"车型号", max_length=64, null=True, blank=True)
    vin_no = models.CharField(verbose_name=u"车架号", max_length=128, blank=True, null=True)
    engine_no = models.CharField(verbose_name=u"发动机号", max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'new_ci_nl_cs_rep'


class MerchantJJ1RepertoryExtend(models.Model):
    """
    jj pailameng
    table extend for MerchantJJ1Repertory
    """
    operator = models.CharField(verbose_name=u'操作者', max_length=64, default='')
    # operator field save who distribute this namelist
    salesman = models.CharField(verbose_name=u'业务员', max_length=64, default='')
    # salesman field save distribute namelist to which account
    is_enable = models.BooleanField(verbose_name=u'是否有效', default=True)
    # when call back this namelist, is_enable=False
    is_assigned = models.BooleanField(verbose_name=u'是否分配', default=False)
    info_status = models.CharField(verbose_name=u'信息状态', max_length=2, default='A',
                                   choices=INFO_STATUS_CHOICES)
    custom_type = models.CharField(verbose_name=u"客户类型", max_length=2, default='A',
                                   choices=CUSTOM_TYPE_CHOICES)
    appoint_time = models.DateTimeField(verbose_name=u'预约时间', default='')
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True, null=True)

    class Meta:
        db_table = 'new_ci_merchant_jj1_rep_ext'


class MerchantJJ1Repertory(models.Model):
    """
    jj pailameng
    namelist come from NameListSZRepertory
    """
    license_no = models.CharField(unique=True, verbose_name=u"车牌号", max_length=64)
    car_brand = models.CharField(verbose_name=u"品牌", max_length=64, null=True, blank=True)
    name = models.CharField(verbose_name=u"客户名", max_length=254, null=True, blank=True)
    tel = models.CharField(verbose_name=u"固定电话", max_length=64, null=True, blank=True)
    phone = models.CharField(verbose_name=u"手机号码", max_length=64, null=True, blank=True)
    address = models.CharField(verbose_name=u"联系地址", max_length=254, null=True, blank=True)
    registered_time = models.DateField(verbose_name=u"登记时间", null=True, blank=True)
    id_no = models.CharField(verbose_name=u"身份证号", max_length=64, null=True, blank=True)
    car_brand_no = models.CharField(verbose_name=u"车型号", max_length=64, null=True, blank=True)
    vin_no = models.CharField(verbose_name=u"车架号", max_length=128, blank=True, null=True)
    engine_no = models.CharField(verbose_name=u"发动机号", max_length=64, blank=True, null=True)
    mjj1r_ext = models.ForeignKey(MerchantJJ1RepertoryExtend, related_name='mjj1r_info',
                                 blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'new_ci_merchant_jj1_rep'


class MerchantJJ2Repertory(models.Model):
    """
    jj renbao
    namelist come from NameListJJRepertory
    """
    license_no = models.CharField(unique=True, verbose_name=u"车牌号", max_length=64)
    car_brand = models.CharField(verbose_name=u"品牌", max_length=64, null=True, blank=True)
    name = models.CharField(verbose_name=u"客户名", max_length=254, null=True, blank=True)
    tel = models.CharField(verbose_name=u"固定电话", max_length=64, null=True, blank=True)
    phone = models.CharField(verbose_name=u"手机号码", max_length=64, null=True, blank=True)
    address = models.CharField(verbose_name=u"联系地址", max_length=254, null=True, blank=True)
    registered_time = models.DateField(verbose_name=u"登记时间", null=True, blank=True)
    id_no = models.CharField(verbose_name=u"身份证号", max_length=64, null=True, blank=True)
    car_brand_no = models.CharField(verbose_name=u"车型号", max_length=64, null=True, blank=True)
    vin_no = models.CharField(verbose_name=u"车架号", max_length=128, blank=True, null=True)
    engine_no = models.CharField(verbose_name=u"发动机号", max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'new_ci_merchant_jj2_rep'


class MerchantJJ3Repertory(models.Model):
    """
    jj tian'an
    namelist come from NameListJJRepertory
    """
    license_no = models.CharField(unique=True, verbose_name=u"车牌号", max_length=64)
    car_brand = models.CharField(verbose_name=u"品牌", max_length=64, null=True, blank=True)
    name = models.CharField(verbose_name=u"客户名", max_length=254, null=True, blank=True)
    tel = models.CharField(verbose_name=u"固定电话", max_length=64, null=True, blank=True)
    phone = models.CharField(verbose_name=u"手机号码", max_length=64, null=True, blank=True)
    address = models.CharField(verbose_name=u"联系地址", max_length=254, null=True, blank=True)
    registered_time = models.DateField(verbose_name=u"登记时间", null=True, blank=True)
    id_no = models.CharField(verbose_name=u"身份证号", max_length=64, null=True, blank=True)
    car_brand_no = models.CharField(verbose_name=u"车型号", max_length=64, null=True, blank=True)
    vin_no = models.CharField(verbose_name=u"车架号", max_length=128, blank=True, null=True)
    engine_no = models.CharField(verbose_name=u"发动机号", max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'new_ci_merchant_jj3_rep'


class MerchantSZ1Repertory(models.Model):
    """
    sz team
    namelist come from NameListSZRepertory
    """
    license_no = models.CharField(unique=True, verbose_name=u"车牌号", max_length=64)
    car_brand = models.CharField(verbose_name=u"品牌", max_length=64, null=True, blank=True)
    name = models.CharField(verbose_name=u"客户名", max_length=254, null=True, blank=True)
    tel = models.CharField(verbose_name=u"固定电话", max_length=64, null=True, blank=True)
    phone = models.CharField(verbose_name=u"手机号码", max_length=64, null=True, blank=True)
    address = models.CharField(verbose_name=u"联系地址", max_length=254, null=True, blank=True)
    registered_time = models.DateField(verbose_name=u"登记时间", null=True, blank=True)
    id_no = models.CharField(verbose_name=u"身份证号", max_length=64, null=True, blank=True)
    car_brand_no = models.CharField(verbose_name=u"车型号", max_length=64, null=True, blank=True)
    vin_no = models.CharField(verbose_name=u"车架号", max_length=128, blank=True, null=True)
    engine_no = models.CharField(verbose_name=u"发动机号", max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'new_ci_merchant_sz1_rep'


class MerchantSD1Repertory(models.Model):
    """
    sd team
    namelist come from NameListSZRepertory
    """
    license_no = models.CharField(unique=True, verbose_name=u"车牌号", max_length=64)
    car_brand = models.CharField(verbose_name=u"品牌", max_length=64, null=True, blank=True)
    name = models.CharField(verbose_name=u"客户名", max_length=254, null=True, blank=True)
    tel = models.CharField(verbose_name=u"固定电话", max_length=64, null=True, blank=True)
    phone = models.CharField(verbose_name=u"手机号码", max_length=64, null=True, blank=True)
    address = models.CharField(verbose_name=u"联系地址", max_length=254, null=True, blank=True)
    registered_time = models.DateField(verbose_name=u"登记时间", null=True, blank=True)
    id_no = models.CharField(verbose_name=u"身份证号", max_length=64, null=True, blank=True)
    car_brand_no = models.CharField(verbose_name=u"车型号", max_length=64, null=True, blank=True)
    vin_no = models.CharField(verbose_name=u"车架号", max_length=128, blank=True, null=True)
    engine_no = models.CharField(verbose_name=u"发动机号", max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'new_ci_merchant_sd1_rep'


class NameListAssignToMerchantRecord(models.Model):
    """
    when assign namelist from NameListXXXRepertory to some merchant repertory
    record the last distribution info;
    """
    repertory_name = models.CharField(max_length=64)  # record namelist come from which rep name
    nl_id = models.CharField(max_length=16)  # record id
    license_no = models.CharField(max_length=64)  # record license_no
    merchant_name = models.CharField(max_length=64)  # save name list divide to which merchant
    operator = models.CharField(verbose_name=u'操作者', max_length=64, default='')
    # save who distribute this namelist
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    class Meta:
        db_table = 'new_ci_nl_to_merchant_record'


class NameListAssignToAccountRecord(models.Model):
    """
    when assign namelist from MerchantXXXRepertory to some account
    record the last distribution info;
    """
    repertory_name = models.CharField(max_length=64)  # record namelist come from which rep name
    nl_id = models.CharField(max_length=16)  # record id
    license_no = models.CharField(max_length=64)  # record license_no
    account_id = models.CharField(max_length=64)  # save name list divide to which account
    operator = models.CharField(verbose_name=u'操作者', max_length=64, default='')
    # save who distribute this namelist
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    class Meta:
        db_table = 'new_ci_nl_to_account_record'