# Generated by Django 5.1.2 on 2024-11-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_product_priceoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priceoffer',
            name='final_price',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='السعر النهائي'),
        ),
    ]
