# Generated by Django 5.0 on 2023-12-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_kitty_image2_kitty_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitty',
            name='image1',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
