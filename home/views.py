import json

from django.contrib.auth import logout, authenticate, login
from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactForm, ContactFormMessage
from order.models import ShopCart
from product.models import Product, Category, Images, Comment


def index(request):
    current_user = request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    popular = Product.objects.all()[:4]
    latest = Product.objects.all().order_by('-id')[:4]
    featured = Product.objects.all().order_by('?')[:4]



    context = {'setting' : setting,
               'sliderdata':sliderdata,
               'category':category,
               'popular':popular,
               'latest':latest,
               'featured':featured,
               }
    return render(request,'index.html',context)

def aboutUs(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,'category':category}
    return render(request, 'aboutus.html', context)

def references(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,'category':category}
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
    category = Category.objects.all()
    form = ContactForm()
    context = {'setting': setting,'form':form,'category':category}
    return render(request, 'contact.html', context)


def category_products(request,id,slug):
    products = Product.objects.filter(category_id=id)
    category_data = Category.objects.get(pk=id)
    category = Category.objects.all()
    context = {'products':products,'category':category,'category_data':category_data}
    return render(request,'products.html',context)


def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id,status='True')

    context = {'product':product,
               'category':category,
               'images':images,
               'comments':comments}
    return render(request, 'product_detail.html', context)


def product_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query'] #formdan bilgiyi al
            products = Product.objects.filter(title__icontains=query) #select * from product title like %query%
            context = {'products':products,'category':category}
            return render(request,'products_search.html',context)
    return HttpResponseRedirect('/')


def product_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        product = Product.objects.filter(title__icontains=q)
        results = []
        for rs in product:
            product_json = {}
            product_json = rs.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
    category = Category.objects.all()
    context = {'category':category,}
    return render(request,'login.html',context)


def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
        return HttpResponseRedirect('/')
    form = SignUpForm()
    category = Category.objects.all()
    context = {'category':category,'form':form}
    return render(request,'register.html',context)