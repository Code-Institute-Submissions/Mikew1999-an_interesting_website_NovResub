# Generated by Django 3.2.7 on 2021-09-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]