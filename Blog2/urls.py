
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blogapp.urls")),
    re_path(r"media/(.*)",serve,{"document_root":settings.MEDIA_ROOT}),
    re_path(r"static/(.*)", serve, {"document_root": settings.STATIC_ROOT})

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)