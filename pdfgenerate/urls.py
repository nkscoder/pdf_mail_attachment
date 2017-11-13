from django.conf.urls import include, url
from . import views
from .views import *

# from product.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
