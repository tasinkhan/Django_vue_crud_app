from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer

@api_view(['GET', 'POST', 'DELETE'])

def product_list(request):
    if request.method=='GET':
        products = Product.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            products = Product.filter(name__icontains=name)
    
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)

    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Product.objects.all().delete()
        return JsonResponse({'message': '{} Products were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
            
        

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        product_serilizer = ProductSerializer(product)
        return JsonResponse(product_serilizer.data)
    
    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(product, data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data)
        return JsonResponse(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': 
        product.delete() 
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
