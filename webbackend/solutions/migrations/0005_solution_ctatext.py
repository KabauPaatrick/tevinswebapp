# Generated by Django 4.2.9 on 2024-03-29 17:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0004_solution_solution_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='ctatext',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
