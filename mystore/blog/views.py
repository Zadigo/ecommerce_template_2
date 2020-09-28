from django.shortcuts import render
from django.views.generic import TemplateView


class PostsView(TemplateView):
    template_name = 'pages/posts.html'


class PostView(TemplateView):
    template_name = 'pages/post.html'
