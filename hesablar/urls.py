from django.conf.urls import url,include
from .views import login_view,register_view,logout_view

app_name = 'hesablar'

urlpatterns = [
    url(r'^giris/$',login_view),
    url(r'^qeydiyyat/$',register_view),
    url(r'^cixis/$',logout_view),
]
