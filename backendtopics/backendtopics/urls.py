from django.contrib import admin
from django.urls import include, path
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('idempotency/', include('idempotentpayment.urls')),
    path('cacheblog/', include('cacheblog.urls')),
    path('blogtest/', include('blogtest.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
