# Generated by Django 5.1.2 on 2024-11-02 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_airconditioner_brand_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم المنتج')),
                ('description', models.TextField(verbose_name='وصف المنتج')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='سعر المنتج')),
            ],
        ),
        migrations.CreateModel(
            name='PriceOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_date', models.DateField(auto_now_add=True, verbose_name='تاريخ العرض')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='الخصم (%)')),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='السعر النهائي')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client', verbose_name='العميل')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product', verbose_name='المنتج')),
            ],
        ),
    ]
