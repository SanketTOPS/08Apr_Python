from django.contrib import admin
from django.urls import path,include
from myapp.views import *

urlpatterns = [
    path('',index),
    path('showdata/',showdata,name='showdata'),
    path('updatedata/<int:id>',updatedata),
    path('deletedata/<int:id>',deletedata),
]