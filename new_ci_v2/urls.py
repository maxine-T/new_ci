from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from new_ci_v2 import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'new_ci_v2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^favicon.ico', RedirectView.as_view(permanent=True, url="/static/favicon.ico")),

    url(r'^admin/', include(admin.site.urls)),
]
