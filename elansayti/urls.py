"""elansayti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from elan.views import elanlar,elaveet,detallar,menimelanlarim,deyisdir,sil,favoritview,favelanlar,komek,haqqinda

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',elanlar,name='base'),
    url(r'^elaveet$',elaveet),
    url(r'^detallar/(?P<id>\d+)/$',detallar),
    url(r'^hesablar/',include('hesablar.urls')),
    url(r'^menimelanlarim/$',menimelanlarim),
    url(r'^deyisdir/(?P<id>\d+)$',deyisdir),
    url(r'^sil/(?P<id>\d+)$',sil),
    url(r'^favorit/(?P<id>\d+)$',favoritview),
    url(r'^favelanlarim$',favelanlar),
    url(r'^komek$',komek),
    url(r'^haqqinda$',haqqinda),
]
handler404 = 'elan.views.page_404'






