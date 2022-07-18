from django.urls import path
from . import views
urlpatterns =[
    path('',views.land,name='land'),
    path('/',views.index,name='index'),
    path('/reg',views.reg,name='reg'),
    path('/home',views.home,name='home'),
    path('/logout',views.logout,name='logout')
]
