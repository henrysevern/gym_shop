# Generated by Django 3.2 on 2023-02-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_item_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.BooleanField(default=False),
        ),
    ]
