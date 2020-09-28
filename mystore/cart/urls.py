from django.conf.urls import url
from cart import views


app_name = 'cart'

urlpatterns = [
    url(r'^checkout$', views.CheckoutView.as_view(), name='checkout'),
    url(r'^$', views.CartView.as_view(), name='home'),
]
