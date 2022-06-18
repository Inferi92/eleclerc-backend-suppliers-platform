from django.forms import JSONField, ValidationError
from django.http import Http404, JsonResponse
from django.shortcuts import render
from rest_framework.schemas import SchemaGenerator
from .models import Color, Supplier, Brand, Product
from .serializers import (
    ColorSerializer,
    SupplierSerializer,
    BrandSerializer,
    ProductSerializer,
)
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


def response_200(serializer):
    return openapi.Response("OK", serializer)


def response_201(serializer):
    return openapi.Response("Successful operation", serializer)


def response_204(serializer):
    return openapi.Response("Successful operation", serializer)


def response_404():
    return openapi.Response("Not Found")


def response_400():
    return openapi.Response("Bad Request")


# Create your views here.

####################### API ENDPOINTS #######################
# All Suppliers
class AllSuppliers(APIView):
    @swagger_auto_schema(
        operation_summary="Obter fornecedores",
        operation_description="Obter todos os fornecedores",
        responses={status.HTTP_200_OK: response_200(SupplierSerializer(many=True))},
    )
    def get(self, request, format=None):
        supplier = Supplier.objects.all()
        serializer = SupplierSerializer(supplier, many=True)
        return JsonResponse(serializer.data, safe=False)

    @swagger_auto_schema(
        operation_summary="Criar um fornecedor",
        operation_description="Criar um novo fornecedor",
        request_body=SupplierSerializer,
        responses={
            status.HTTP_201_CREATED: response_201(SupplierSerializer),
            status.HTTP_400_BAD_REQUEST: response_400(),
        },
    )
    def post(self, request, format=None):
        supplier = SupplierSerializer(data=request.data)
        if supplier.is_valid():
            supplier.save()
            return Response(supplier.data, status=status.HTTP_201_CREATED)
        return Response(supplier.errors, status=status.HTTP_400_BAD_REQUEST)


# Supplier by NIF
class SingleSupplier(APIView):
    def get_object(self, nif):
        try:
            return Supplier.objects.get(nif=nif)
        except Supplier.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Obter fornecedor pelo seu NIF",
        operation_description="Obter um fornecedor específico",
        responses={
            status.HTTP_200_OK: response_200(SupplierSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def get(self, request, nif, format=None):
        supplier = self.get_object(nif)
        serializer = SupplierSerializer(supplier)
        return JsonResponse(serializer.data, safe=False)

    @swagger_auto_schema(
        operation_summary="Atualizar um fornecedor pelo seu NIF",
        operation_description="Atualizar um fornecedor específico",
        request_body=SupplierSerializer,
        responses={
            status.HTTP_200_OK: response_200(SupplierSerializer),
            status.HTTP_400_BAD_REQUEST: response_400(),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def put(self, request, nif, format=None):
        supplier = self.get_object(nif)
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Apagar um fornecedor pelo seu NIF",
        operation_description="Apagar um fornecedor específico",
        responses={
            status.HTTP_204_NO_CONTENT: response_204(SupplierSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def delete(self, request, nif, format=None):
        supplier = self.get_object(nif)
        supplier.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


# All Brands
class AllBrands(APIView):
    @swagger_auto_schema(
        operation_summary="Obter marcas",
        operation_description="Obter todos os marcas",
        responses={status.HTTP_200_OK: response_200(BrandSerializer(many=True))},
    )
    def get(self, request, format=None):
        brand = Brand.objects.all()
        serializer = BrandSerializer(brand, many=True)
        return JsonResponse(serializer.data, safe=False)

    @swagger_auto_schema(
        operation_summary="Criar uma marca",
        operation_description="Criar uma nova marca",
        request_body=BrandSerializer,
        responses={
            status.HTTP_201_CREATED: response_201(BrandSerializer),
            status.HTTP_400_BAD_REQUEST: response_400(),
        },
    )
    def post(self, request, format=None):
        brand = BrandSerializer(data=request.data)
        if brand.is_valid():
            brand.save()
            return Response(brand.data, status=status.HTTP_201_CREATED)
        return Response(brand.errors, status=status.HTTP_400_BAD_REQUEST)


# Brand by ID
class SingleBrand(APIView):
    def get_object(self, name):
        try:
            return Brand.objects.get(name=name)
        except Brand.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Obter marca pelo seu Nome",
        operation_description="Obter uma marca específica",
        responses={
            status.HTTP_200_OK: response_200(BrandSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def get(self, request, name, format=None):
        brand = self.get_object(name)
        serializer = BrandSerializer(brand)
        return JsonResponse(serializer.data, safe=False)

    @swagger_auto_schema(
        operation_summary="Atualizar um marca pelo seu Nome",
        operation_description="Atualizar um marca específica",
        request_body=BrandSerializer,
        responses={
            status.HTTP_200_OK: response_200(BrandSerializer),
            status.HTTP_400_BAD_REQUEST: response_400(),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def put(self, request, name, format=None):
        brand = self.get_object(name)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Apagar um marca pelo seu Nome",
        operation_description="Apagar um marca específico",
        responses={
            status.HTTP_204_NO_CONTENT: response_204(BrandSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def delete(self, request, pk, format=None):
        brand = self.get_object(pk)
        brand.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


# Brand by Supplier
class BrandBySupplier(APIView):
    def get_object(self, nif):
        try:
            return Supplier.objects.get(nif=nif)
        except Supplier.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Obter marcas por fornecedor",
        operation_description="Obter marcas de um fornecedor específico",
        responses={
            status.HTTP_200_OK: response_200(BrandSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def get(self, request, nif, format=None):
        products = Brand.objects.filter(supplier=nif)
        serializer = BrandSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


# All Products
class AllProducts(APIView):
    @swagger_auto_schema(
        operation_summary="Obter produtos",
        operation_description="Obter todos os produtos",
        responses={status.HTTP_200_OK: response_200(ProductSerializer(many=True))},
    )
    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)

    @swagger_auto_schema(
        operation_summary="Criar um produto",
        operation_description="Criar um novo produto",
        request_body=ProductSerializer,
        responses={
            status.HTTP_201_CREATED: response_201(ProductSerializer),
            status.HTTP_400_BAD_REQUEST: response_400(),
        },
    )
    def post(self, request, format=None):
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response(product.data, status=status.HTTP_201_CREATED)
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)


# Product by ID
class SingleProduct(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Obter um produto pelo seu ID",
        operation_description="Obter um produto específico",
        responses={
            status.HTTP_200_OK: response_200(ProductSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data, safe=False)

    @swagger_auto_schema(
        operation_summary="Atualizar um produto pelo seu ID",
        operation_description="Atualizar um produto específico",
        request_body=ProductSerializer,
        responses={
            status.HTTP_200_OK: response_200(ProductSerializer),
            status.HTTP_400_BAD_REQUEST: response_400(),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Apagar um produto pelo seu ID",
        operation_description="Apagar um produto específico",
        responses={
            status.HTTP_204_NO_CONTENT: response_204(ProductSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


# Product by Supplier
class ProductBySupplier(APIView):
    def get_object(self:Supplier, nif):
        try:
            return Supplier.objects.get(nif=nif)
        except Supplier.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Obter produtos por fornecedor",
        operation_description="Obter produtos de um fornecedor específico",
        responses={
            status.HTTP_200_OK: response_200(ProductSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def get(self, request, nif, format=None):
        products = Product.objects.filter(supplier=nif)
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


# Top 20 Products by Supplier
class TopTwentyProducts(APIView):
    def get_object(self:Supplier, nif):
        try:
            return Supplier.objects.get(nif=nif)
        except Supplier.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Obter TOP 20 produtos por fornecedor",
        operation_description="Obter os últimos 20 produtos criados de um fornecedor específico",
        responses={
            status.HTTP_200_OK: response_200(ProductSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def get(self, request, nif, format=None):
        products = Product.objects.filter(supplier=nif).order_by("created_date")[:20]
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


# Number of Discontinued Products by Supplier
class NumberOfDiscontinuedProducts(APIView):
    def get_object(self:Supplier, nif):
        try:
            return Supplier.objects.get(nif=nif)
        except Supplier.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Obter o número de produtos descontinuados por fornecedor",
        operation_description="Obter o número produtos descontinuados de um fornecedor específico",
        responses={
            status.HTTP_200_OK: response_200(serializers.Serializer(ProductSerializer)),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def get(self, request, nif, format=None):
        products = Product.objects.filter(supplier=nif).filter(discontinued=True).count()
        return JsonResponse(products, safe=False)

# Discontinued Products by Supplier
class DiscontinuedProducts(APIView):
    def get_object(self:Supplier, nif):
        try:
            return Supplier.objects.get(nif=nif)
        except Supplier.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Obter os produtos descontinuados por fornecedor",
        operation_description="Obter todos os produtos descontinuados de um fornecedor específico",
        responses={
            status.HTTP_200_OK: response_200(ProductSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def get(self, request, nif, format=None):
        products = Product.objects.filter(supplier=nif).filter(discontinued=True)
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

# Number of Blocked Products by Supplier
class NumberOfBlockedProducts(APIView):
    def get_object(self:Supplier, nif):
        try:
            return Supplier.objects.get(nif=nif)
        except Supplier.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Obter o número de produtos bloqueados por fornecedor",
        operation_description="Obter o número produtos bloqueados de um fornecedor específico",
        responses={
            status.HTTP_200_OK: response_200(ProductSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def get(self, request, nif, format=None):
        products = Product.objects.filter(supplier=nif).filter(bloqueado=True).count()
        return JsonResponse(products, safe=False)

# Blocked Products by Supplier
class BlockedProducts(APIView):
    def get_object(self:Supplier, nif):
        try:
            return Supplier.objects.get(nif=nif)
        except Supplier.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Obter os produtos bloqueados por fornecedor",
        operation_description="Obter todos os produtos bloqueados de um fornecedor específico",
        responses={
            status.HTTP_200_OK: response_200(ProductSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def get(self, request, nif, format=None):
        products = Product.objects.filter(supplier=nif).filter(bloqueado=True)
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


# Number of Brands by Supplier
class NumberOfBrandsBySupplier(APIView):
    def get_object(self:Supplier, nif):
        try:
            return Supplier.objects.get(nif=nif)
        except Supplier.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Obter o número de marcas por fornecedor",
        operation_description="Obter o número de marcas de um fornecedor específico",
        responses={
            status.HTTP_200_OK: response_200(BrandSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def get(self, request, nif, format=None):
        products = Brand.objects.filter(supplier=nif).count()
        return JsonResponse(products, safe=False)

# All Colors
class AllColors(APIView):
    @swagger_auto_schema(
        operation_summary="Obter cores",
        operation_description="Obter todos as cores",
        responses={status.HTTP_200_OK: response_200(ColorSerializer(many=True))},
    )
    def get(self, request, format=None):
        color = Color.objects.all()
        serializer = ColorSerializer(color, many=True)
        return JsonResponse(serializer.data, safe=False)

    @swagger_auto_schema(
        operation_summary="Criar uma cor",
        operation_description="Criar uma nova cor",
        request_body=ColorSerializer,
        responses={
            status.HTTP_201_CREATED: response_201(ColorSerializer),
            status.HTTP_400_BAD_REQUEST: response_400(),
        },
    )
    def post(self, request, format=None):
        color = ColorSerializer(data=request.data)
        if color.is_valid():
            color.save()
            return Response(color.data, status=status.HTTP_201_CREATED)
        return Response(color.errors, status=status.HTTP_400_BAD_REQUEST)


# Color by ID
class SingleColor(APIView):
    def get_object(self, name):
        try:
            return Color.objects.get(name=name)
        except Color.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Obter uma cor pelo seu Nome",
        operation_description="Obter uma cor específica",
        responses={
            status.HTTP_200_OK: response_200(ColorSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def get(self, request, name, format=None):
        color = self.get_object(name)
        serializer = ColorSerializer(color)
        return JsonResponse(serializer.data, safe=False)

    @swagger_auto_schema(
        operation_summary="Atualizar uma cor pelo seu Nome",
        operation_description="Atualizar uma cor específica",
        request_body=ColorSerializer,
        responses={
            status.HTTP_200_OK: response_200(ColorSerializer),
            status.HTTP_400_BAD_REQUEST: response_400(),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def put(self, request, name, format=None):
        color = self.get_object(name)
        serializer = ColorSerializer(color, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Apagar uma cor pelo seu Nome",
        operation_description="Apagar uma cor específica",
        responses={
            status.HTTP_204_NO_CONTENT: response_204(ColorSerializer),
            status.HTTP_404_NOT_FOUND: response_404(),
        },
    )
    def delete(self, request, name, format=None):
        color = self.get_object(name)
        color.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )
