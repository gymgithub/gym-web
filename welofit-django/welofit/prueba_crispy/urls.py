from django.conf.urls import url

from prueba_crispy import views

urlpatterns = [
    url(r'^$', views.prueba, name='prueba'),
]