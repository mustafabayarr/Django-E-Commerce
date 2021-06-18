from django.contrib import admin

# Register your models here.
from home.models import Setting, ContactFormMessage, UserProfile, FAQ

admin.site.register(Setting)

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message','note','status']
    list_filter = ['status']

admin.site.register(ContactFormMessage,ContactFormAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','image_tag','phone','address','city','country']
admin.site.register(UserProfile,UserProfileAdmin)

class FAQAdmin(admin.ModelAdmin):
    list_display =['ordernumber','question','answer','status']
    list_filter =['status']
admin.site.register(FAQ,FAQAdmin)

