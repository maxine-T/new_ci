from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from new_ci_namelist_management.views import *


urlpatterns = [
    url(r'^list/sz/$', login_required(SZNameListView.as_view(),
        login_url='/login/'), name='sz_namelist_manage_home'),

    url(r'^assign/batch/sz/$', login_required(SZNameListAssignBatch.as_view(),
        login_url='/login/'), name='sz_namelist_assign_batch'),
]
