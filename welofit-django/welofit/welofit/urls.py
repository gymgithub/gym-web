from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('registro.urls')),
    url(r'^diets/', include('diets_generator.urls')),
    url(r'^monitor/', include('monitor.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
