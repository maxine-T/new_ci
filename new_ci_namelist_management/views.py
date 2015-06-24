# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import *
from forms import *
import time
import logging
logger = logging.getLogger('namelist_management')


class SZNameListView(TemplateView):
    template_name = 'sz_namelist_repertory.html'

    def get_context_data(self):
        logger.debug("hello~")
        nl_sz_rep = NameListSZRepertory.objects.all()
        logger.info("nl_sz_rep is: %s" % nl_sz_rep)
        logger.info("nl_sz_rep count is: %s" % nl_sz_rep.count())
        return {'msg': u'welcome, namelist manage begin', 'nl_sz_rep': nl_sz_rep}


class SZNameListAssignBatch(TemplateView):
    template_name = 'sz_namelist_assign_batch.html'

    def get_context_data(self):
        init_start_at = time.strftime("%Y-%m-%d")
        return {
            'init_start_at': init_start_at,
            'msg': 'hello~',
            'form': NameListAssignBatchForm()
        }

    def post(self, request):
        start_at = request.POST.get('start_at', '')
        end_at = request.POST.get('end_at', '')

        result = MerchantJJ1Repertory.objects.select_related('merchantjj1repertoryextend') \
            .filter(mjj1r_ext__is_enable=True, mjj1r_ext__is_assigned=False).count()
        print "111===>>>"
        print result
        print "222===>>>"

        data = {'msg': 'post success~', 'result': result}
        return JsonResponse(data)