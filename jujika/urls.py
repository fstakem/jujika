from django.conf.urls import include, url
from django.contrib import admin
from jujika import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.landing, name='jujika.views.landing'),
    url(r'^(?P<user_name>.*)/', include('socialnet.urls')),
]
