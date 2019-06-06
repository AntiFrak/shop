from django.shortcuts import render
from django.core.mail import send_mail

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
                order = form.save()
                for item in cart:
                        OrderItem.objects.create(order=order, product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
                cart.clear()
                send_mail('Nowe zamówienie', 'Nowe zamówienie dodane do admin panelu', 
                        'sklepszkielety@gmail.com', ['yangrodno@yandex.ru'], fail_silently=False)
                return render(request, 'orders/order/created.html', {'order':order})
    
    form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form':form})
