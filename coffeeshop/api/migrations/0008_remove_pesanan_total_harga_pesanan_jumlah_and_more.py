# Generated by Django 5.0.4 on 2024-07-07 10:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_pesanan_menu_alter_pesanan_total_harga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesanan',
            name='total_harga',
        ),
        migrations.AddField(
            model_name='pesanan',
            name='jumlah',
            field=models.IntegerField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pesanan',
            name='menu',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, related_name='pesanan', to='api.menu'),
            preserve_default=False,
        ),
    ]
