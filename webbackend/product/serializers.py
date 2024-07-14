from rest_framework import serializers
from .models import Product, ProductImage, Color, Category, Brand
from cloudinary.models import CloudinaryField


class ProductImageSerializer(serializers.ModelSerializer):
    file = serializers.ImageField(write_only=True)

    class Meta:
        model = ProductImage
        fields = ['file']

    def create(self, validated_data):
        file = validated_data.pop('file')
        product_image = ProductImage.objects.create(file=file, **validated_data)
        return product_image

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        product = Product.objects.create(**validated_data)
        
        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)

        return product
