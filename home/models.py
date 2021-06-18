from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe


class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True,max_length=150)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=55)
    smtpserver = models.CharField(blank=True,max_length=30)
    smtpemail = models.CharField(blank=True,max_length=30)
    smtppassword = models.CharField(blank=True,max_length=30)
    smtpport = models.CharField(blank=True,max_length=30)
    icon = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(blank=True, max_length=30)
    instagram = models.CharField(blank=True, max_length=30)
    youtube = models.CharField(blank=True, max_length=30)
    twitter = models.CharField(blank=True, max_length=30)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.title

class ContactFormMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
    )
    name = models.CharField(max_length=150,blank=True)
    email = models.CharField(max_length=150,blank=True)
    subject = models.CharField(max_length=150,blank=True)
    message = models.CharField(max_length=255,blank=True)
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(max_length=25,blank=True)
    note = models.CharField(max_length=125,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name','email','subject','message']
        widgets = {
            'name' : TextInput(attrs={'class': 'form-control','placeholder':'Your Name'}),
            'subject' : TextInput(attrs={'class': 'form-control','placeholder':'Subject'}),
            'email' : TextInput(attrs={'class': 'form-control','placeholder':'Email'}),
            'message' : Textarea(attrs={'class': 'form-control','placeholder':'Message'})
        }

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(blank=True,max_length=20)
    address = models.CharField(blank=True,max_length=50)
    city = models.CharField(blank=True,max_length=20)
    country = models.CharField(blank=True,max_length=20)
    image = models.ImageField(blank=True,upload_to='images/users/')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return '[' + self.user.username + '] ' + self.user.first_name + ' ' + self.user.last_name

    def image_tag(self):
        if self.image:
         return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
    image_tag.short_description = 'Image'

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone','address','city','country','image']

class FAQ(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=150,blank=True)
    answer = models.TextField(max_length=150,blank=True)
    status = models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.question

