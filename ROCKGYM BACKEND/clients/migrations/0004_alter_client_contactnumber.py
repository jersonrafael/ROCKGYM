# Generated by Django 5.0.4 on 2024-05-01 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_client_enddate_alter_client_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contactNumber',
            field=models.CharField(max_length=200),
        ),
    ]
