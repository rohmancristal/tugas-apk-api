# Generated by Django 5.0.4 on 2024-07-07 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_pesanan_total_harga_pesanan_jumlah_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pesanan',
            old_name='jumlah',
            new_name='total_harga',
        ),
    ]
