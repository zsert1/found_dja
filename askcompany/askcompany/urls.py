
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('instagram/', include('instagram.urls')),
    path('accounts/', include('accounts.urls'))

]
# 미디어 파일 읽어오기
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
