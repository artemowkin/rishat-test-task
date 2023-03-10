# Generated by Django 4.1.6 on 2023-02-10 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_discount_alter_tax_description_order_discounts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="discounts",
            field=models.ManyToManyField(null=True, to="orders.discount"),
        ),
        migrations.AlterField(
            model_name="order",
            name="taxes",
            field=models.ManyToManyField(null=True, to="orders.tax"),
        ),
    ]
