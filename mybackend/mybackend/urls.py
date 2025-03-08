from django.contrib import admin
from django.urls import path, include
from myapp.views import home  # 匯入 home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/animals/', include('myapp.urls')),
    path('', home, name='home'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
