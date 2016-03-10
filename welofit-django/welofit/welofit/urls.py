from django.conf.urls import include, url
from django.contrib import admin
import registro
from registro import views

urlpatterns = [
    url(r'^$', registro.views.register_wizard, name='register_wizard'),
    url(r'^diets/', include('diets_generator.urls')),
    url(r'^monitor/', include('monitor.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
