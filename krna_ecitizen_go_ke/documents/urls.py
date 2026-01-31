from django.urls import path
from .views import verify_document, root_redirect
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', root_redirect),  # root redirect
    path(
        "ecitizen/api/applications/<uuid:application_id>/outputs/<uuid:output_id>/verify",
        verify_document,
        name="verify_document",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
