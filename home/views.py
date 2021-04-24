from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from home.models import Setting, ContactForm, ContactFormMessage
from product.models import Product


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    context = {'setting' : setting,'sliderdata':sliderdata}
    return render(request,'index.html',context)

def aboutUs(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'aboutus.html', context)

def references(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'references.html', context)

def contact(request):

    if request.method == 'POST': #form post edildiyse
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage() #model ile bağlantı kur
            data.name = form.cleaned_data['name'] #formdan bilgileri al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save() #veritabanında kaydet
            messages.success(request,"Send succesfully.")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactForm()
    context = {'setting': setting,'form':form}
    return render(request, 'contact.html', context)