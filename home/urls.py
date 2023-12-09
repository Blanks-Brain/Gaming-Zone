from django.urls import path,include
from . import views

urlpatterns=[
    path("",views.homepage,name="home-page"),
    path("index",views.index,name="index-page"),
    
]
