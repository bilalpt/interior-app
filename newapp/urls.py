from django.urls import path,include
from . import views

urlpatterns = [
    path('one',views.app,name='one'),
    path('one1',views.app1,name='one1'),
    path('one2',views.app2,name='one2'),
    path('one3',views.app3,name='one3'),
    path('one4',views.app4,name='one4')
]
