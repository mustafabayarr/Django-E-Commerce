from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile
from order.models import Order, OrderProduct
from product.models import Category, Comment, Product, ProductForm, ProductImageForm, Images
from user.forms import UserUpdateForm, ProfileUpdateForm

@login_required(login_url='/login')
def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category, 'profile': profile}
    return render(request, 'user_profile.html', context)

@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user_update.html', context)

@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return HttpResponseRedirect('change_password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request,'change_password.html',{'form':form,'category':category})

@login_required(login_url='/login')
def orders(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    orders = Order.objects.filter(user_id=current_user.id)
    context = {
        'category':category,
        'orders':orders,
        'profile': profile
    }
    return render(request,"user_orders.html",context)

@login_required(login_url='/login')
def orderdetail(request,id):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    order = Order.objects.get(user_id=current_user.id,id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    context = {
        'category': category,
        'order': order,
        'profile': profile,
        'orderitems': orderitems
    }
    return render(request, "user_order_detail.html", context)

@login_required(login_url='/login')
def comments(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'comments': comments,
        'profile': profile
    }
    return render(request, "user_comments.html", context)

@login_required(login_url='/login')
def deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id,user_id=current_user.id).delete()

    return HttpResponseRedirect('/user/comments')

@login_required(login_url='/login')
def contents(request):
    category = Category.objects.all()
    current_user = request.user
    product = Product.objects.filter(user_id=current_user.id)
    context = {
        'category':category,
        'product':product
    }
    return render(request,'user_contents.html',context)
@login_required(login_url='/login')
def addcontent(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Product()
            data.user_id = current_user.id
            data.category = form.cleaned_data['category']
            data.title = form.cleaned_data['title']
            data.slug = form.cleaned_data['slug']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.price = form.cleaned_data['price']
            data.amount = form.cleaned_data['amount']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.save()
            return HttpResponseRedirect('/user/contents')
        else:
            HttpResponseRedirect('/user/addcontents')
    else:
        category = Category.objects.all()
        form = ProductForm()
        context = {
            'category':category,
            'form':form
        }
        return render(request,'user_addcontents.html',context)

@login_required(login_url='/login')
def contentedit(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/contents')
        else:
            HttpResponseRedirect('/user/addcontents')
    else:
        category = Category.objects.all()
        form = ProductForm(instance=product)
        context = {
            'category': category,
            'form': form
        }
        return render(request,'user_addcontents.html',context)

@login_required(login_url='/login')
def contentdelete(request,id):
    current_user = request.user
    Product.objects.filter(id=id,user_id=current_user.id).delete()
    return HttpResponseRedirect('/user/contents')

@login_required(login_url='/login')
def contentaddimage(request,id):
    if request.method == 'POST':
        lasturl = request.META.get('HTTP_REFERER')
        form = ProductImageForm(request.POST,request.FILES)
        if form.is_valid():
            data = Images()
            data.title = form.cleaned_data['title']
            data.product_id = id
            data.image = form.cleaned_data['image']
            data.save()
            return HttpResponseRedirect(lasturl)
        else:
            return HttpResponseRedirect(lasturl)
    else:
        product = Product.objects.get(id=id)
        images = Images.objects.filter(product_id=id)
        form = ProductImageForm()
        context = {
            'product':product,
            'images':images,
            'form':form
        }
        return render(request,'content_gallery.html',context)
