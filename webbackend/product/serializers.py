from rest_framework import serializers
from .models import Product, ProductImage, Color, Category, Brand
import cloudinary.uploader

class ProductImageSerializer(serializers.ModelSerializer):
    file = serializers.ImageField()

    class Meta:
        model = ProductImage
        fields = ['file', 'id', 'asset_id', 'public_id']

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

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', None)
        instance = super().update(instance, validated_data)

        if images_data:
            # Update existing images and create new ones if they don't exist
            existing_images = {image.id: image for image in instance.images.all()}
            for image_data in images_data:
                image_id = image_data.get('id')
                if image_id and image_id in existing_images:
                    existing_image = existing_images.pop(image_id)
                    for attr, value in image_data.items():
                        setattr(existing_image, attr, value)
                    existing_image.save()
                else:
                    ProductImage.objects.create(product=instance, **image_data)
            
            # Delete images that were not included in the new data
            for image in existing_images.values():
                image.delete()

        return instance
