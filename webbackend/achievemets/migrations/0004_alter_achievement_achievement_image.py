# Generated by Django 4.2.9 on 2024-04-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievemets', '0003_achievement_achievement_image_achievement_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='achievement_image',
            field=models.FileField(blank=True, null=True, upload_to='media/achievement_images/'),
        ),
    ]
