from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    textt = "Merhaba"
    context = {'texttt' : textt}
    return render(request,'index.html',context)
