from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from new_ci_namelist_management.views import *


urlpatterns = [
    url(r'^list/$', login_required(NameListView.as_view(),
        login_url='/login/'), name='namelist_manage_home'),

    url(r'^assign/batch/$', login_required(NameListAssignBatch.as_view(),
        login_url='/login/'), name='namelist_assign_batch'),
]
