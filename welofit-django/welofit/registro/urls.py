from django.conf.urls import url

import registro
from registro import views


urlpatterns = [
    url(r'^$', views.register_wizard, name='register_wizard'),
    url(r'^registro/$', views.register_data, name='register_data'),
]