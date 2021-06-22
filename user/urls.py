from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('addcomment/<int:id>',views.addcomment,name='addcomment')
    path('update/', views.user_update, name="user_update"),
    path('password/', views.change_password, name="change_password"),
    path('orders/', views.orders, name="orders"),
    path('orderdetail/<int:id>', views.orderdetail, name="orderdetail"),
    path('comments/', views.comments, name="comments"),
    path('deletecomment/<int:id>', views.deletecomment, name="deletecomment"),
    path('contents/',views.contents,name="contents"),
    path('addcontent/',views.addcontent,name="addcontent"),
    path('contentedit/<int:id>',views.contentedit,name="contentedit"),
    path('contentdelete/<int:id>',views.contentdelete,name="contentdelete"),
    path('contentaddimage/<int:id>',views.contentaddimage,name="contentaddimage"),
]
