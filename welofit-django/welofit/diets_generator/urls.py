from django.conf.urls import url

from diets_generator import views

urlpatterns = [
    url(r'^$', views.dashboard_generator, name='dashboard_generator'),
    url(r'^compute/$', views.compute, name='compute'),
    url(r'^optimize/$', views.optimize, name='optimize'),
    url(r'^find/$', views.find, name='find'),

]

