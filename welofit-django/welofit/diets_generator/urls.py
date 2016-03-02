from django.conf.urls import url

from diets_generator import views

urlpatterns = [
    url(r'^$', views.dashboard_generator, name='dashboard_generator'),
    url(r'^sol/$', views.sol, name='sol'),
    url(r'^foods/$', views.food_name, name='foods'),
]

