# Generated by Django 4.2.9 on 2024-03-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homeview', '0002_homeview_created_at_homeview_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeview',
            name='image',
            field=models.ImageField(upload_to='media/homeview_images/'),
        ),
    ]
