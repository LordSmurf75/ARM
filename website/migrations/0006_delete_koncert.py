# Generated by Django 4.2.6 on 2023-10-23 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_spillested_alter_bestyrelse_options_koncert'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Koncert',
        ),
    ]
