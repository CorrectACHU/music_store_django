# Generated by Django 3.2.9 on 2021-11-04 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_earphonesproduct_wireless'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earphonesproduct',
            name='wireless',
            field=models.BooleanField(default=False, verbose_name='Беспроводные'),
        ),
    ]
