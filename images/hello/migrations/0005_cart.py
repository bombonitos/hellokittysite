# Generated by Django 5.0 on 2023-12-25 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_kitty_category_kitty_price_kitty_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('kitty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.kitty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.user')),
            ],
        ),
    ]
