from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("", include(("clinica.urls", "clinica"), namespace="clinica")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / "static")

handler404 = "clinica.views.pagina_inexistente"
handler500 = "clinica.views.erro_servidor"