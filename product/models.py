import uuid

import self as self
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, Select, TextInput, FileInput, forms,ChoiceField
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    STATUS = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=100,blank=True)
    keywords = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=255,blank=True)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=10,choices=STATUS)
    slug = models.SlugField(unique=True,null=False)
    parent = TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self): #alt kategoriler
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '->'.join(full_path[::-1])

    #def image_tag(self):
     #   return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    #image_tag.short_description = 'Image'

    def image_tag(self):
         if self.image:
             #return mark_safe(f'<img src="{self.image.url}" height="50"/>')
             return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
         else:
             return ""

    def get_absolute_url(self):
        return reverse('category_detail',kwargs={'slug':self.slug})


class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE) #relation with Category table  .. category_id .. CASCADE category id silindimi alt elemanlarıyla beraber sil demek.
    title = models.CharField(max_length=100,blank=True)
    slug = models.SlugField(unique=True,null=False)
    keywords = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=255,blank=True)
    image = models.ImageField(blank=True,upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.title

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('product_detail',kwargs={'slug':self.slug})

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category','title','slug','keywords','description','image','price','amount','detail']
        widgets = {
            'category': Select(),
            'title' : TextInput(attrs={'class':'input','placeholder':'title'}),
            'slug' : TextInput(attrs={'class':'input','placeholder':'slug'}),
            'keywords' : TextInput(attrs={'class':'input','placeholder':'keywords'}),
            'description' : TextInput(attrs={'class':'input','placeholder':'description'}),
            'image' :FileInput(attrs={'class':'input','placeholder':'image'}),
            'price': TextInput(attrs={'class': 'input', 'placeholder': 'price'}),
            'amount': TextInput(attrs={'class': 'input', 'placeholder': 'amount'}),
            'detail': CKEditorWidget()
        }


class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True) #blank = True alanı boş bırakabiliriz anlamına gelir.
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return  self.title

    def image_tag(self):
        if self.image:
         return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
    image_tag.short_description = 'Image'

class ProductImageForm(ModelForm):
    class Meta:
        model = Images
        fields = ['title','image']


class Comment(models.Model):
    STATUS = (
        ('New','Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100,blank=True)
    comment = models.TextField(max_length=100,blank=True)
    rate = models.IntegerField(blank=True)
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject','comment','rate']




