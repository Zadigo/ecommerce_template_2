from django.shortcuts import render
from django.views.generic import TemplateView

class HeroView(TemplateView):
    template_name = 'pages/home.html'
