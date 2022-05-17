from django.urls import path
from platform_api import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="E.Leclerc Suppliers Platform API",
        default_version="v2",
        description="Documentação da API da Plataforma de Fornecedores do E.Leclerc",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # URLS API ENDPOINTS
    path("api/fornecedor/<int:pk>", views.FornecedorDetailAPI.as_view(), name="single_supplier_api"),
    path("api/fornecedor/", views.FornecedorPOST.as_view(), name="add_single_supplier_api"),
    path("api/marca/<int:pk>", views.MarcaDetailAPI.as_view(), name="single_brand_api"),
    path("api/marca/", views.MarcaPOST.as_view(), name="add_single_brand_api"),

    path("api/docs", schema_view.with_ui("swagger", cache_timeout=0)),
]
