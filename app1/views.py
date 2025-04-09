from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def electronics_all(request):
    electronics = Electronics.objects.all()
    serializers = ElectronicsSerializer(electronics, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def electronics_one(request, electronic_id):
    try:
        electronic = Electronics.objects.get(electronic_id = electronic_id)
        serializers = ElectronicsSerializer(electronic, many = False)
        return Response(serializers.data)
    except:
        return Response(serializers.errors)

@api_view(['POST'])
def add_product(request):
    serializers = ElectronicsSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors)

@api_view(['DELETE'])
def del_electronics(request, electronic_id):
    try:
        el = Electronics.objects.get(electronic_id = electronic_id)
        el.delete()
        return Response("Deleted Successfully")
    except:
        return Response("Invalid!!")

@api_view(['PUT'])
def electronic_update(request, electronic_id):
    try:
        el = Electronics.objects.get(electronic_id = electronic_id)
        ser = ElectronicsSerializer(el, data = request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    except:
        return Response(ser.errors)
