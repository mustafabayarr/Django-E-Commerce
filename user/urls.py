from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('addcomment/<int:id>',views.addcomment,name='addcomment')
    path('update/',views.user_update,name="user_update"),
    path('password/',views.change_password,name="change_password"),
    path('orders/',views.orders,name="orders"),
    path('orderdetail/<int:id>',views.orderdetail,name="orderdetail")
]