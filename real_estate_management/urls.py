
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.urls import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', RedirectView.as_view(url=reverse_lazy('login_page')), name='home'),
    path('api/auth/', include('users.urls')),
    path('api/', include('estates.urls')),
    path('api/rental-agreements/', include('rentalAgreements.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
