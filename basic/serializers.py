from rest_framework import serializers
from .models import ProductInfo


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo
        fields = [
            'code',
            'name',
            'model',
            'createtime',
            'modifytime',
        ]
        read_only_fields = [
            'createtime',
        ]
        extra_kwargs = {"type": {"write_only": True}}
