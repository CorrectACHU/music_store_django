# Generated by Django 3.2.9 on 2021-11-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211103_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='earphonesproduct',
            name='cable_len',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Длина кабеля'),
        ),
    ]
