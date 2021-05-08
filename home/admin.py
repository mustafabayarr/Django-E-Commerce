from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage, UserProfile

admin.site.register(Setting)

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message','note','status']
    list_filter = ['status']

admin.site.register(ContactFormMessage,ContactFormAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','image_tag','phone','address','city','country']
admin.site.register(UserProfile,UserProfileAdmin)
