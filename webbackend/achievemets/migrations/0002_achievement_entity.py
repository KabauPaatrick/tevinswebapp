# Generated by Django 4.2.9 on 2024-01-31 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0001_initial'),
        ('achievemets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='entity',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='entity.entity'),
        ),
    ]
