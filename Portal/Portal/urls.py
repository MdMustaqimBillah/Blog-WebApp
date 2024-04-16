
from django.contrib import admin
from django.urls import path,include
from Blog_App import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('authentication/',include('Authentication_App.urls')),
    path('blog/',include('Blog_App.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)