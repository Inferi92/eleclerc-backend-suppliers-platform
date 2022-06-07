from django.urls import path
from platform_api import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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
    path(
        "api/fornecedor/<int:nif>",
        views.SingleSupplier.as_view(),
        name="single_supplier_api",
    ),
    path("api/fornecedor/", views.AllSuppliers.as_view(), name="suppliers_api"),
    path("api/marca/<str:name>", views.SingleBrand.as_view(), name="single_brand_api"),
    path("api/marca/", views.AllBrands.as_view(), name="brands_api"),
    path(
        "api/marca/fornecedor/<int:nif>",
        views.BrandBySupplier.as_view(),
        name="brands_by_supplier_api",
    ),
    path(
        "api/produto/<int:pk>", views.SingleProduct.as_view(), name="single_product_api"
    ),
    path("api/produto/", views.AllProducts.as_view(), name="products_api"),
    path(
        "api/produto/fornecedor/<int:nif>",
        views.ProductBySupplier.as_view(),
        name="products_by_supplier_api",
    ),
    path("api/cor/<str:name>", views.SingleColor.as_view(), name="single_color_api"),
    path("api/cor/", views.AllColors.as_view(), name="colors_api"),
    path("api/docs", schema_view.with_ui("swagger", cache_timeout=0)),
]
