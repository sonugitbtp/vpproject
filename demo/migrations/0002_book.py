# Generated by Django 5.0.2 on 2024-02-28 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_books', to='demo.author')),
            ],
        ),
    ]