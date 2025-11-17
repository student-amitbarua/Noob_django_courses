from django.contrib import admin
from .models import ContactUs

# Register your models here.

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone' , 'problem'] # admin site model e list row te show korve

admin.site.register(ContactUs, ContactModelAdmin)