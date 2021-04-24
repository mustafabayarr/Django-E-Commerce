from django.shortcuts import render

from django.http import HttpResponse

from home.models import Setting


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting' : setting}
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
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'contact.html', context)