# -*- coding: utf-8 -*-
from django import forms


class NameListAssignBatchForm(forms.Form):
    # start_at = forms.DateField(label=u'开始日期')
    # end_at = forms.DateField(label=u'结束日期')
    merchant = forms.CharField(max_length=64, label=u'商户名')   # save merchant id
    team = forms.CharField(max_length=64, label=u'团队名')   # save team id
    group = forms.CharField(max_length=64, label=u'小组名')   # save group id
    salesman = forms.CharField(max_length=254, label=u'业务员')   # save salesman id
    assign_count = forms.IntegerField(max_value=30, min_value=1, label=u'分配数量')