from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from .views import *

urlpatterns = [
    path('upd/', upload, name='upload'),
    path('get/', show_image, name='image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
