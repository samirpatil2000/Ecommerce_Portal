# Generated by Django 4.0.6 on 2022-08-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_cart_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='upload/products/'),
        ),
    ]
