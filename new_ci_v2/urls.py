from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from new_ci_v2 import views
from new_ci_v2.forms import AuthenticationForm

urlpatterns = [
    # Examples:
    # url(r'^$', 'new_ci_v2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^favicon.ico', RedirectView.as_view(permanent=True, url="/static/favicon.ico")),

    url(r'^account/', include('new_ci_account.urls')),

    url(r'^login/$', 'django.contrib.auth.views.login',
        {
            "template_name": "login.html",
            "authentication_form": AuthenticationForm,
        }, name="auth_login"),

    url(r'^admin/', include(admin.site.urls)),
]
