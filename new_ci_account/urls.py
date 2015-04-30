from django.conf.urls import url
from new_ci_account import views


urlpatterns = [
    url(r'^home/$', views.AccountHomeView.as_view(), name='account_home'),
]