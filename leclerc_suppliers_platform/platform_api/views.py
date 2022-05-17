from django.http import Http404, JsonResponse
from django.shortcuts import render
from .models import Cores, Fornecedor, Marca, Produto
from .serializers import CoresSerializer, FornecedorSerializer, MarcaSerializer

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
    return openapi.Response("Successful operation")


def response_404(serializer):
    return openapi.Response("Not Found")


def response_400(serializer):
    return openapi.Response("Bad Request")


# Create your views here.

####################### API ENDPOINTS #######################
# Fornecedor by ID
class FornecedorDetailAPI(APIView):
    def get_object(self, nif):
        try:
            return Fornecedor.objects(nif=nif)
        except Fornecedor.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Obter fornecedor pelo seu NIF",
        operation_description="Obter um fornecedor específico",
        responses={
            status.HTTP_200_OK: response_200(FornecedorSerializer),
            status.HTTP_404_NOT_FOUND: response_404(FornecedorSerializer),
        },
    )
    def get(self, request, nif, format=None):
        fornecedor = self.get_object(nif)
        serializer = FornecedorSerializer(fornecedor)
        return JsonResponse(serializer.data, safe=False)

    @swagger_auto_schema(
        operation_summary="Atualizar um fornecedor pelo seu NIF",
        operation_description="Atualizar um fornecedor específico",
        responses={
            status.HTTP_200_OK: response_200(FornecedorSerializer),
            status.HTTP_400_BAD_REQUEST: response_400(FornecedorSerializer),
            status.HTTP_404_NOT_FOUND: response_404(FornecedorSerializer),
        },
    )
    def put(self, request, nif, format=None):
        fornecedor = self.get_object(nif)
        serializer = FornecedorSerializer(fornecedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Apagar um fornecedor pelo seu NIF",
        operation_description="Apagar um fornecedor específico",
        responses={
            status.HTTP_204_NO_CONTENT: response_204(FornecedorSerializer),
            status.HTTP_404_NOT_FOUND: response_404(FornecedorSerializer),
        },
    )
    def delete(self, request, nif, format=None):
        fornecedor = self.get_object(nif)
        fornecedor.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


class FornecedorPOST(APIView):
    @swagger_auto_schema(
        operation_summary="Criar um Fornecedor",
        operation_description="Criar um novo Fornecedor",
        request_body=FornecedorSerializer,
        responses={
            status.HTTP_201_CREATED: response_201(FornecedorSerializer),
            status.HTTP_400_BAD_REQUEST: response_400(FornecedorSerializer),
        },
    )
    def post(self, request, format=None):
        fornecedor = FornecedorSerializer(data=request.data)
        if fornecedor.is_valid():
            fornecedor.save()
            return Response(fornecedor.data, status=status.HTTP_201_CREATED)
        return Response(fornecedor.errors, status=status.HTTP_400_BAD_REQUEST)


# Marca by ID
class MarcaDetailAPI(APIView):
    def get_object(self, pk):
        try:
            return Marca.objects(pk=pk)
        except Marca.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Obter Marca pelo seu ID",
        operation_description="Obter uma Marca específica",
        responses={
            status.HTTP_200_OK: response_200(MarcaSerializer),
            status.HTTP_404_NOT_FOUND: response_404(MarcaSerializer),
        },
    )
    def get(self, request, pk, format=None):
        marca = self.get_object(pk)
        serializer = MarcaSerializer(marca)
        return JsonResponse(serializer.data, safe=False)

    @swagger_auto_schema(
        operation_summary="Atualizar um Marca pelo seu ID",
        operation_description="Atualizar um Marca específico",
        responses={
            status.HTTP_200_OK: response_200(MarcaSerializer),
            status.HTTP_400_BAD_REQUEST: response_400(MarcaSerializer),
            status.HTTP_404_NOT_FOUND: response_404(MarcaSerializer),
        },
    )
    def put(self, request, pk, format=None):
        marca = self.get_object(pk)
        serializer = MarcaSerializer(marca, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Apagar um Marca pelo seu ID",
        operation_description="Apagar um Marca específico",
        responses={
            status.HTTP_204_NO_CONTENT: response_204(MarcaSerializer),
            status.HTTP_404_NOT_FOUND: response_404(MarcaSerializer),
        },
    )
    def delete(self, request, pk, format=None):
        marca = self.get_object(pk)
        marca.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )


class MarcaPOST(APIView):
    @swagger_auto_schema(
        operation_summary="Criar uma marca",
        operation_description="Criar uma nova marca",
        request_body=MarcaSerializer,
        responses={
            status.HTTP_201_CREATED: response_201(MarcaSerializer),
            status.HTTP_400_BAD_REQUEST: response_400(MarcaSerializer),
        },
    )
    def post(self, request, format=None):
        marca = MarcaSerializer(data=request.data)
        if marca.is_valid():
            marca.save()
            return Response(marca.data, status=status.HTTP_201_CREATED)
        return Response(marca.errors, status=status.HTTP_400_BAD_REQUEST)
