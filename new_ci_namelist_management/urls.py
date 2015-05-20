from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from new_ci_namelist_management.views import NameListView


urlpatterns = [
    url(r'^list/$', login_required(NameListView.as_view(),
        login_url='/login/'), name='namelist_manage_home'),
]
