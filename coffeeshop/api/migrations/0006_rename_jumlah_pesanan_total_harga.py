# Generated by Django 5.0.4 on 2024-07-07 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_pesanan_total_harga'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pesanan',
            old_name='jumlah',
            new_name='total_harga',
        ),
    ]
