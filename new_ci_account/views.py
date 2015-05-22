# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
# from django.shortcuts import render


class AccountHomeView(TemplateView):
    # template_name = 'home.html'
    template_name = 'base_home.html'

    def get_context_data(self, **kwargs):
        return {'msg': u'welcome, index page, too~'}
