# Generated by Django 5.0 on 2023-12-27 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0009_kitty_image1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('card_number', models.CharField(max_length=16)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
    ]
