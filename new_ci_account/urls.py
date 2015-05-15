from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from new_ci_account import views


urlpatterns = [
    url(r'^home/$', login_required(views.AccountHomeView.as_view(),
        login_url='/login/'), name='account_home'),
]