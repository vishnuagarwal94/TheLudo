# Generated by Django 5.0.2 on 2024-06-05 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ludoapp', '0011_withdrawalaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawalaccount',
            name='withdraw_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
