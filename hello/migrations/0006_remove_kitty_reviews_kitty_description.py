# Generated by Django 5.0 on 2023-12-26 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitty',
            name='reviews',
        ),
        migrations.AddField(
            model_name='kitty',
            name='description',
            field=models.CharField(default='', max_length=5000),
        ),
    ]