from django.contrib import admin
from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('food_item_list/', views.food_item_list, name='food_item_list'),
    path('order/', views.order, name='order'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/orders/',views.admin_order_list, name='admin_order_list'),

]

