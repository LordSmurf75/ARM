# Generated by Django 4.2.6 on 2024-07-04 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_frivillig_options_koncert_band6_koncert_band7_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='koncert',
            name='billetter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='koncert',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
    ]
