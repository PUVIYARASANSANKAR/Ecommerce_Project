# Generated by Django 5.0 on 2023-12-25 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_products_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='catagory',
        ),
    ]
