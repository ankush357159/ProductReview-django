from reviews.models import Category, Product
from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils.timezone import now

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    # If the field is used to represent a to-many relationship, many=True flag to be added to the serializer field.
    class Meta:
        model = Product
        fields = ['pk', 'name', 'category']


class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days
