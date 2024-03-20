# Generated by Django 5.0.2 on 2024-02-16 15:04

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prod_Cat_Item_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=255)),
                ('item_image', models.ImageField(upload_to='items_images/')),
                ('item_rec_qty', models.IntegerField(blank=True)),
                ('item_rec_date', models.DateField(default=datetime.date.today)),
                ('item_price', models.IntegerField(blank=True)),
                ('Hsn_code', models.IntegerField(blank=True)),
                ('prod_cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.prod_category')),
            ],
        ),
    ]