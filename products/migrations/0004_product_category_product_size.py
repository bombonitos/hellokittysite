# Generated by Django 5.0 on 2023-12-22 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
    ]