# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
# from django.shortcuts import render


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {'msg': u'welcome, index page, too~'}
