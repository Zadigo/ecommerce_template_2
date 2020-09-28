from django.conf.urls import url
from shop import views

app_name = 'shop'

urlpatterns = [
    url(r'^single-product$', views.ProductView.as_view(), name='product'),
    url(r'^$', views.ProductsView.as_view(), name='products'),
]
