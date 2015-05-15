# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
import logging
logger = logging.getLogger('django')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        host = self.request.get_host()
        logger.debug("The host is ===>: %s", host)
        return {'msg': u'welcome, index page, too~'}