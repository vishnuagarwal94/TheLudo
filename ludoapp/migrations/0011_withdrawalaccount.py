# Generated by Django 5.0.2 on 2024-06-05 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ludoapp', '0010_battle_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='withdrawalaccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder_name', models.CharField(max_length=255)),
                ('upi_id', models.CharField(max_length=255)),
                ('confirm_upi_id', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ludoapp.player')),
            ],
        ),
    ]
