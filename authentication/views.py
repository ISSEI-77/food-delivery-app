from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FoodItem, Category, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required


# Authentication views
def home(request):
    fname = request.user.first_name if request.user.is_authenticated else ''
    context = {
        'fname': fname,
    }
    return render(request, "index.html",context)

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 characters!!")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!!")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been created successfully!!")
        return redirect('signin')

    return render(request, "signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('signin')
    return render(request, "signin.html")

def signout(request):
    logout(request)
    # messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

# Admin view for orders
@staff_member_required
def admin_order_list(request):
    orders = Order.objects.filter(is_ordered=True).prefetch_related('orderitem_set', 'user')
    context = {
        'orders': orders,
    }
    return render(request, 'admin_order_list.html', context)

# Food item list view
def food_item_list(request):
    categories = Category.objects.all()
    categorized_items = {}
    for category in categories:
        items = FoodItem.objects.filter(category=category, is_available=True)
        categorized_items[category] = items
    return render(request, 'food_item_list.html', {'categorized_items': categorized_items})


# Order views
@login_required
def order(request):
    current_order = Order.objects.filter(user=request.user, is_ordered=False).first()
    order_items = OrderItem.objects.filter(order=current_order) if current_order else []
    total_price = sum(item.price * item.quantity for item in order_items)

    context = {
        'order': current_order,
        'order_items': order_items,
        'total_price': total_price,
        
    }
    return render(request, 'order.html', context)

@login_required
def place_order(request):
    current_order = Order.objects.filter(user=request.user, is_ordered=False).first()
    if current_order:
        current_order.is_ordered = True
        current_order.save()
        return redirect('order_confirmation')
    else:
        messages.warning(request, 'No active order found.')
        return redirect('order')

@login_required
def order_confirmation(request):
    return render(request, 'order_confirmation.html')

@login_required
def delete_item(request, item_id):
    OrderItem.objects.filter(id=item_id).delete()
    return redirect('order')

@login_required
def delete_from_cart(request, item_id):
    item = get_object_or_404(OrderItem, id=item_id)
    item.delete()
    return redirect('order')

@login_required
def add_to_cart(request, item_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        food_item = get_object_or_404(FoodItem, id=item_id)

        order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)

        order_item, created = OrderItem.objects.get_or_create(order=order, item=food_item)
        if created:
            order_item.quantity = quantity
            order_item.price = food_item.price
        else:
            order_item.quantity += quantity
            if not order_item.price:
                order_item.price = food_item.price
        order_item.save()

        return redirect('order')
    return redirect('food_item_list')
