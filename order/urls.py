from django.urls import path, re_path

from order import views

urlpatterns=[
    path('',views.index, name='index'),
    path('addtocart/<int:id>/',views.addtocart,name='addtocart'),
    path('deletefromcart/<int:id>/',views.deletefromcart,name='deletefromcart')

]