from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage

admin.site.register(Setting)

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message','note','status']
    list_filter = ['status']

admin.site.register(ContactFormMessage,ContactFormAdmin)