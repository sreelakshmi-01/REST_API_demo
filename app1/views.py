from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def electronics_all(request):
    electronics = Electronics.objects.all()
    serializers = ElectronicsSerializer(electronics, many=True)
    return Response(serializers.data)

@api_view(['POST'])
def add_product(request):
    serializers = ElectronicsSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)