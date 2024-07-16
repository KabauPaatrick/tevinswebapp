from rest_framework import serializers
from .models import Product, ProductImage, Color, Category, Brand

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'title', 'created_at', 'updated_at']

class ProductImageSerializer(serializers.ModelSerializer):
    file = serializers.ImageField()

    class Meta:
        model = ProductImage
        fields = ['id', 'file', 'asset_id', 'public_id']

    def create(self, validated_data):
        file = validated_data.pop('file')
        upload_data = cloudinary.uploader.upload(file)
        validated_data.update({
            'asset_id': upload_data.get('asset_id'),
            'public_id': upload_data.get('public_id')
        })
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'file' in validated_data:
            file = validated_data.pop('file')
            upload_data = cloudinary.uploader.upload(file)
            validated_data.update({
                'asset_id': upload_data.get('asset_id'),
                'public_id': upload_data.get('public_id')
            })
        return super().update(instance, validated_data)

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    colors = ColorSerializer(read_only=True, many=True)
    brand = serializers.SlugRelatedField(slug_field='title', queryset=Brand.objects.all())
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'price', 'category', 'brand', 'quantity', 'sold', 'images', 'colors', 'tags', 'total_ratings', 'ratings', 'created_at', 'updated_at']

class SingleProductResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    data = ProductSerializer()
    message = serializers.CharField()
