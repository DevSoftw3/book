from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.bookapp.views import Error404View, Error505View
from config import settings

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.bookapp.urls')),
    path('', include('apps.login.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    path('social-auth/', include('social_django.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = Error404View.as_view()
handler500 = Error505View.as_error_view()