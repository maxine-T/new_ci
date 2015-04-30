# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
# from django.shortcuts import render
import logging
logger = logging.getLogger('django')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        host=self.request.get_host()
        logger.debug(host)
        print "===222===", host
        return {'msg': u'welcome, index page, too~'}
