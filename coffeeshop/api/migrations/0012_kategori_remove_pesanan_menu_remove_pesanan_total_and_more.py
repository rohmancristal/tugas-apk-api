# Generated by Django 5.0.4 on 2024-07-07 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_pesanan_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='pesanan',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='pesanan',
            name='total',
        ),
        migrations.AddField(
            model_name='pelanggan',
            name='poin_loyalitas',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pesanan',
            name='total_harga',
            field=models.DecimalField(decimal_places=2, default=12, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='kategori',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.kategori'),
            preserve_default=False,
        ),
    ]
