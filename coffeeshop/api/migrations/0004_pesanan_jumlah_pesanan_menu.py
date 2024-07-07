# Generated by Django 5.0.4 on 2024-07-07 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_kategori_remove_menu_kategori_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesanan',
            name='jumlah',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pesanan',
            name='menu',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='pesanan', to='api.menu'),
            preserve_default=False,
        ),
    ]
