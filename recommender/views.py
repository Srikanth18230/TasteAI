from django.shortcuts import render, redirect
from .models import Cart
from datetime import datetime

FOOD_PRICES = {
    "burger": 40,
    "coke": 20,
    "pasta": 60,
    "biryani": 150,
    "cold_coffee": 70,
    "mandi": 250,
    "diet_coke": 45,
    "sweet": 30
}

# First page
def landing(request):
    return render(request, "landing.html")


# Menu page
def home(request):
    cart_items = Cart.objects.all()

    total = 0
    cart_count = 0

    item_counts = {
        "burger": 0,
        "coke": 0,
        "pasta": 0,
        "biryani": 0,
        "cold_coffee": 0,
        "mandi": 0,
        "diet_coke": 0,
        "sweet": 0
    }

    for item in cart_items:
        total += item.price * item.quantity
        cart_count += item.quantity

        if item.food_name in item_counts:
            item_counts[item.food_name] += item.quantity

    return render(request, "home.html", {
        "cart_count": cart_count,
        "total": total,
        "item_counts": item_counts
    })


def add_item(request, food_name):
    item = Cart.objects.filter(food_name=food_name).first()

    if item:
        item.quantity += 1
        item.save()
    else:
        Cart.objects.create(
            food_name=food_name,
            quantity=1,
            price=FOOD_PRICES[food_name]
        )

    return redirect('/menu/')


def remove_item(request, food_name):
    item = Cart.objects.filter(food_name=food_name).first()

    if item:
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()

    return redirect('/menu/')


def checkout(request):
    cart_items = Cart.objects.all()

    total = 0
    for item in cart_items:
        total += item.price * item.quantity

    current_time = datetime.now()

    return render(request, "checkout.html", {
        "cart_items": cart_items,
        "total": total,
        "current_time": current_time
    })