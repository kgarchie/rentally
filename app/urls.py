from os import name
from django.urls.conf import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

app_name = 'app'

urlpatterns = [
    path('', views.index, name='home'),
    path('add_house', views.add_house, name='add_house'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

