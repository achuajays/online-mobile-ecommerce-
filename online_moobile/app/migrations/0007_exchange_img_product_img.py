# Generated by Django 5.0.1 on 2024-01-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='img',
            field=models.ImageField(default=1, upload_to='img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=1, upload_to='media'),
            preserve_default=False,
        ),
    ]
