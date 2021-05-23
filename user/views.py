from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile
from product.models import Category
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = { 'category': category,'profile':profile}
    return render(request,'user_profile.html',context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category':category,
            'user_form':user_form,
            'profile_form':profile_form
        }
        return render(request,'user_update.html',context)


def change_password(request):
    return None