# Generated by Django 5.1.3 on 2024-11-16 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "ecommerce2",
            "0001_squashed_0005_remove_productmodel_short_description",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="productmodel",
            name="state",
            field=models.CharField(
                choices=[
                    ("BR", "BORRADO"),
                    ("PU", "PUBLICADO"),
                    ("PR", "PRIVADO"),
                ],
                default="BR",
                max_length=2,
            ),
        ),
    ]
