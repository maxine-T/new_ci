from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from new_ci_v2.forms import AuthenticationForm
from new_ci_account.views import AccountHomeView

urlpatterns = [
    # Examples:
    # url(r'^$', 'new_ci_v2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', login_required(AccountHomeView.as_view(),
        login_url='/login/'), name='account_home'),

    url(r'^favicon.ico', RedirectView.as_view(permanent=True, url="/static/favicon.ico")),

    url(r'^account/', include('new_ci_account.urls')),

    url(r'^namelist_management/', include('new_ci_namelist_management.urls')),

    url(r'^login/$', 'django.contrib.auth.views.login',
        {
            "template_name": "login.html",
            "authentication_form": AuthenticationForm,
        }, name="auth_login"),

    url(r'^logout/$', 'django.contrib.auth.views.logout', {"template_name": "login.html"},
        name="auth_logout"
        ),

    url(r'^admin/', include(admin.site.urls)),
]
