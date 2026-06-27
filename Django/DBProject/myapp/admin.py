from django.contrib import admin
from .models import *

# Register your models here.
class Userdata(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','name','email','mobile']

admin.site.register(Userinfo,Userdata)
