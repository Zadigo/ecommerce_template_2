from django.conf.urls import url
from blog import views


app_name = 'blog'

urlpatterns = [
    url(r'^post$', views.PostView.as_view(), name='post'),
    url(r'^posts$', views.PostsView.as_view(), name='posts'),
]
