from rest_framework import serializers
from .models import *

class ElectronicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = electronics
        fields = '__all__'
