from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #Django admin
    path('goose/', admin.site.urls),

    #User management
    path('accounts/', include('allauth.urls')),

    #Local apps
    path('books/', include('books.urls')),
    path('', include('pages.urls')),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

