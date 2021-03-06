from rest_framework import serializers, viewsets, status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .serializers import ProductSerializer
import random

class ProductViewSet(viewsets.ViewSet):
    def list(self, request): #/api/products
        products = Product.object.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
        
    def create(self, request): #/api/products
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrive(self, request, pk=None): #/api/products<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None): #/api/products<str:id>
        product = Product.object.get(id=pk)
        serializer = ProductSerializer(isinstance=product, data=request.data)
        serializer.is_valid(raise_exceptio=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): #/api/products<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choices(users)
        return Response({
            'id': user.id
        })