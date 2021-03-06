from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('main/', include('main.urls')),
    path('weather/', include('weather.urls')),
    path('contacts/', include('contacts.urls')),
    path('translate/', include('translate.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
