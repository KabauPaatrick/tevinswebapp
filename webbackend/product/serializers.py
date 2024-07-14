from rest_framework import serializers
from .models import Product, ProductImage, Color, Category, Brand
import cloudinary

class ProductImageSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['file_url', 'asset_id', 'public_id']

    def get_file_url(self, obj):
        return obj.file.url

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'title', 'created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    colors = ColorSerializer()
    category = serializers.CharField(source='category.title')
    brand = serializers.CharField(source='brand.title')

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description', 'slug', 'price', 'category', 'brand',
            'quantity', 'sold', 'images', 'colors', 'tags', 'total_ratings',
            'ratings', 'created_at', 'updated_at'
        ]

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        colors_data = validated_data.pop('colors')
        category_title = validated_data.pop('category')['title']
        brand_title = validated_data.pop('brand')['title']

        category, created = Category.objects.get_or_create(title=category_title)
        brand, created = Brand.objects.get_or_create(title=brand_title)
        color, created = Color.objects.get_or_create(id=colors_data['id'], defaults=colors_data)
        
        product = Product.objects.create(
            category=category,
            brand=brand,
            colors=color,
            **validated_data
        )

        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)

        return product

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', None)
        colors_data = validated_data.pop('colors', None)
        category_title = validated_data.pop('category', {}).get('title')
        brand_title = validated_data.pop('brand', {}).get('title')

        if category_title:
            category, created = Category.objects.get_or_create(title=category_title)
            instance.category = category

        if brand_title:
            brand, created = Brand.objects.get_or_create(title=brand_title)
            instance.brand = brand

        if colors_data:
            color, created = Color.objects.get_or_create(id=colors_data['id'], defaults=colors_data)
            instance.colors = color

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.sold = validated_data.get('sold', instance.sold)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.total_ratings = validated_data.get('total_ratings', instance.total_ratings)
        instance.ratings = validated_data.get('ratings', instance.ratings)
        instance.save()

        if images_data:
            instance.images.all().delete()
            for image_data in images_data:
                ProductImage.objects.create(product=instance, **image_data)

        return instance
