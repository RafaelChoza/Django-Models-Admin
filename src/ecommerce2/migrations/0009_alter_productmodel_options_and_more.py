# Generated by Django 5.1.3 on 2024-11-16 21:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "ecommerce2",
            "0008_rename_product_dimentions_productmodel_product_dimensions_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productmodel",
            options={"ordering": ["-update", "-timestamp"]},
        ),
        migrations.AddField(
            model_name="productmodel",
            name="publish_timestamp",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="productmodel",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="productmodel",
            name="update",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
