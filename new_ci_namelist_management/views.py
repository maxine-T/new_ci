# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.shortcuts import render
import logging
logger = logging.getLogger('namelist_management')


class NameListView(TemplateView):
    template_name = 'namelist_repertory.html'

    def get_context_data(self, **kwargs):
        logger.debug("hello~")
        return {'msg': u'welcome, namelist manage begin'}



