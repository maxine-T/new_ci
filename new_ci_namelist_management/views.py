# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import *
from forms import *
import logging
logger = logging.getLogger('namelist_management')


class NameListView(TemplateView):
    template_name = 'namelist_repertory.html'

    def get_context_data(self, **kwargs):
        logger.debug("hello~")
        nl_sz_rep = NameListSZRepertory.objects.all()
        logger.info("nl_sz_rep is: %s" % nl_sz_rep)
        logger.info("nl_sz_rep count is: %s" % nl_sz_rep.count())
        return {'msg': u'welcome, namelist manage begin', 'nl_sz_rep': nl_sz_rep}


class NameListAssignBatch(TemplateView):
    template_name = 'namelist_assign_batch.html'

    def get_context_data(self, **kwargs):
        return {
            'msg': 'hello~',
            'form': NameListAssignBatchForm()
        }