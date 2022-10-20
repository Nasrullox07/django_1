from django.contrib import admin
from myfiles.models import *
# Register your models here.

class Works(admin.ModelAdmin):
    list_display = ['id','nomi','manzil','rasm','xona1','xona2','kv','narx_new']
admin.site.register(Work,Works)

class Client(admin.ModelAdmin):
    list_display = ['id','ismi','ishi','men_haqimda','rasm']
admin.site.register(Clients,Client)

class Agent(admin.ModelAdmin):
    list_display = ['id','name','mulki','rasm']
admin.site.register(Agents,Agent)

class Oxirgi_ish(admin.ModelAdmin):
    list_display = ['id','rasm','malumot','sana']
admin.site.register(Oxirgi_ishlar,Oxirgi_ish)

class AdminM(admin.ModelAdmin):
    list_display = ['id','ism','mail','sub','mess','vaqt']
admin.site.register(Murojaat,AdminM)