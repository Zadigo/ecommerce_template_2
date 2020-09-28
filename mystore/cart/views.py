from django.shortcuts import render
from django.views.generic import TemplateView

class CartView(TemplateView):
    template_name = 'pages/cart.html'


class CheckoutView(TemplateView):
    template_name = 'pages/checkout.html'
