"""arhiv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from arhivator.views import index, signup
from django.views.generic.base import TemplateView
# from arhivator import views as core_views

urlpatterns = [
    ...

]


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^login/$', auth_views.login,{'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', signup, name='signup'),
    url(r'^home/', TemplateView.as_view(template_name='home.html'), name='home'),


]
