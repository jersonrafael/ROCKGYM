# Generated by Django 5.0.4 on 2024-05-01 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_alter_classes_date_alter_plains_endtime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='classEnd',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='classes',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]
