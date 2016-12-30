from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib import admin

urlpatterns = [
    url(r'^', TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'^example/$', TemplateView.as_view(template_name="example.html"), name="example"),
    url(r'^admin/', admin.site.urls),
]
