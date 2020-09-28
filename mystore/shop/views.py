from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.html import mark_safe

import random

class ProductView(TemplateView):
    template_name = 'pages/product.html'


class ProductsView(TemplateView):
    template_name = 'pages/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = [
            [i, f'/media/img/shop/shop-{i}.jpg'] for i in range(1, 10)
        ]
        random.shuffle(images)
        context['products'] = images
        return context
