# Generated by Django 5.0.4 on 2024-05-01 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_plains_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='plains',
            name='status',
            field=models.BooleanField(default=bool),
        ),
    ]
