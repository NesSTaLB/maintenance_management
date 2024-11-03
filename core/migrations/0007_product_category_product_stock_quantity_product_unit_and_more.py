# Generated by Django 5.1.2 on 2024-11-02 21:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_priceoffer_final_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='التصنيف'),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='الكمية المتوفرة'),
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(default='قطعة', max_length=50, verbose_name='الوحدة'),
        ),
        migrations.CreateModel(
            name='NewPriceOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_date', models.DateField(auto_now_add=True, verbose_name='تاريخ العرض')),
                ('expiration_date', models.DateField(blank=True, null=True, verbose_name='تاريخ انتهاء العرض')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='الخصم (%)')),
                ('final_price', models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='السعر النهائي')),
                ('status', models.CharField(choices=[('Active', 'نشط'), ('Expired', 'منتهي الصلاحية'), ('Used', 'مستخدم')], default='Active', max_length=20, verbose_name='حالة العرض')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client', verbose_name='العميل')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product', verbose_name='المنتج')),
            ],
        ),
        migrations.DeleteModel(
            name='PriceOffer',
        ),
    ]
