# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.checks import messages

# Create your views here.
from django.utils.crypto import get_random_string

from home.models import UserProfile
from order.models import ShopCartForm, ShopCart, OrderForm, Order, OrderProduct
from product.models import Category, Product


def index(request):
    return HttpResponse("Order App")


@login_required(login_url='/login')
def addtocart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkproduct = ShopCart.objects.filter(product_id=id)

    if checkproduct:
        control = 1
    else:
        control = 0

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
                request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
                return HttpResponseRedirect(url)
    else:
        if control == 1:
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
            request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    schopcart = ShopCart.objects.filter(user_id=current_user.id)
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()

    total = 0
    for rs in schopcart:
        total += rs.product.price * rs.quantity
    context = {
        'schopcart': schopcart,
        'category': category,
        'total': total
    }
    return render(request, 'shopcart_products.html', context)


@login_required(login_url='/login')
def deletefromcart(request, id):
    ShopCart.objects.filter(id=id).delete()
    current_user = request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    return HttpResponseRedirect('/shopcart')


@login_required(login_url='/login')
def orderproduct(request):
    category = Category.objects.all()
    current_user = request.user
    schopcart = ShopCart.objects.filter(user_id=current_user.id)

    total = 0
    for rs in schopcart:
        total += rs.product.price * rs.quantity

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.country = form.cleaned_data['country']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.country = form.cleaned_data['country']
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()

            schopcart = ShopCart.objects.filter(user_id=current_user.id)
            for rs in schopcart:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                # Reduce quantity of sold product from amount of product
                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()

                detail.price = rs.product.price
                detail.amount = rs.amount
                detail.save()

            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items'] = 0
            return render(request, 'order_completed.html', {'ordercode': ordercode, 'category': category})
        else:
            return HttpResponseRedirect('/order/orderproduct')
    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'schopcart': schopcart,
        'category': category,
        'total': total,
        'form': form,
        'profile': profile
    }
    return render(request,'order_form.html',context)
