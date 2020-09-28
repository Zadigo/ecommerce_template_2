from django.shortcuts import render
from django.views.generic import TemplateView

class ProductView(TemplateView):
    template_name = 'pages/product.html'


class ProductsView(TemplateView):
    template_name = 'pages/products.html'
