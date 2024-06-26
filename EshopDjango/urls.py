from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('cs/admin/', admin.site.urls),
                  path('cs/', include('Eshop.urls')),
                  path('cs/kosik/', include('Kosik.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
