# from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin
# from authentication.models import  Category, FoodItem,CustomUser
# # Register your models here.

# from .models import FoodItem, Order, OrderItem

# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     extra = 0

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('user','is_ordered' ,'created_at')
#     inlines = [OrderItemInline]

# admin.site.register(Order)
# admin.site.register(OrderItem)
# admin.site.register(CustomUser)

# # admin.site.register(Product)
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']

# @admin.register(FoodItem)
# class FoodItemAdmin(admin.ModelAdmin):
#     list_display = ['name', 'category', 'price', 'is_available', 'rating', 'created_at', 'updated_at']
#     list_filter = ['category', 'is_available']
#     search_fields = ['name', 'description']
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .models import CustomUser, Category, FoodItem, Order, OrderItem

class UserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(CustomUser, UserAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_ordered', 'created_at','date')
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available', 'rating', 'created_at', 'updated_at']
    list_filter = ['category', 'is_available']
    search_fields = ['name', 'description']