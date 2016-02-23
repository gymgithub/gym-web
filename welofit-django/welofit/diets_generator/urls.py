from django.conf.urls import url

from diets_generator import views

urlpatterns = [
    url(r'^$', views.dashboard_generator, name='dashboard_generator'),
]

