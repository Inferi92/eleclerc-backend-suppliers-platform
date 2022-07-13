from django.urls import include, path
from platform_api import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="E.Leclerc Suppliers Platform API",
        default_version="v2.2",
        description="Documentação da API da Plataforma de Fornecedores do E.Leclerc",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # URLS API ENDPOINTS
    path(
        "api/fornecedor/<int:nif>",
        views.SingleSupplier.as_view(),
        name="single_supplier_api",
    ),
    path("api/fornecedor/", views.AllSuppliers.as_view(), name="suppliers_api"),
    path(
        "api/marca/<int:nif>/<str:name>",
        views.SingleBrand.as_view(),
        name="single_brand_api",
    ),
    path("api/marca/", views.AllBrands.as_view(), name="brands_api"),
    path(
        "api/marca/fornecedor/<int:nif>",
        views.BrandBySupplier.as_view(),
        name="brands_by_supplier_api",
    ),
    path(
        "api/produto/<int:nif>/<int:ean>",
        views.SingleProduct.as_view(),
        name="single_product_api",
    ),
    path("api/produto/", views.AllProducts.as_view(), name="products_api"),
    path(
        "api/produto/fornecedor/<int:nif>",
        views.ProductBySupplier.as_view(),
        name="products_by_supplier_api",
    ),
    path(
        "api/estatisticas/topvinte/fornecedor/<int:nif>",
        views.TopTwentyProducts.as_view(),
        name="top_twenty_products_by_supplier_api",
    ),
    path(
        "api/estatisticas/produtos/fornecedor/<int:nif>",
        views.NumberOfProducts.as_view(),
        name="number_of_products_by_supplier_api",
    ),
    path(
        "api/estatisticas/descontinuados/fornecedor/<int:nif>",
        views.DiscontinuedProducts.as_view(),
        name="discontinued_products_by_supplier_api",
    ),
    path(
        "api/estatisticas/ndescontinuados/fornecedor/<int:nif>",
        views.NumberOfDiscontinuedProducts.as_view(),
        name="number_of_discontinued_products_by_supplier_api",
    ),
    path(
        "api/estatisticas/bloqueados/fornecedor/<int:nif>",
        views.BlockedProducts.as_view(),
        name="blocked_products_by_supplier_api",
    ),
    path(
        "api/estatisticas/nbloqueados/fornecedor/<int:nif>",
        views.NumberOfBlockedProducts.as_view(),
        name="number_of_blocked_products_by_supplier_api",
    ),
    path(
        "api/estatisticas/nmarcas/fornecedor/<int:nif>",
        views.NumberOfBrandsBySupplier.as_view(),
        name="number_of_brands_by_supplier_api",
    ),
    path(
        "api/estatisticas/ativos/fornecedor/<int:nif>",
        views.ActiveProducts.as_view(),
        name="active_products_by_supplier_api",
    ),
    path(
        "api/estatisticas/nativos/fornecedor/<int:nif>",
        views.NumberOfActiveProducts.as_view(),
        name="number_of_active_products_by_supplier_api",
    ),
    path("api/cor/<str:name>", views.SingleColor.as_view(), name="single_color_api"),
    path("api/cor/", views.AllColors.as_view(), name="colors_api"),
    path("api/docs", schema_view.with_ui("swagger", cache_timeout=0)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
