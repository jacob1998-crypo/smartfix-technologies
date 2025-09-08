
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path("", include("Main.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
