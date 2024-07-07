# Generated by Django 5.0.4 on 2024-07-07 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_jumlah_pesanan_total_harga'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesanan',
            name='menu',
        ),
        migrations.AlterField(
            model_name='pesanan',
            name='total_harga',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]