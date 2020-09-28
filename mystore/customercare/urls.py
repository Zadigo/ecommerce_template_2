from django.conf.urls import url
from customercare import views

app_name = 'customercare'

urlpatterns = [
    url(r'^contact$', views.ContactView.as_view(), name='contact')
]
