from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Rest Framework GUI
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    # API
    path('api/', include('api.urls'), name='api')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)