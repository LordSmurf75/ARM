# Generated by Django 4.2.6 on 2023-10-23 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_delete_koncert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Koncert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(max_length=255)),
                ('dato', models.DateTimeField()),
                ('facebook', models.URLField()),
                ('billetter', models.URLField()),
                ('band1', models.CharField(max_length=255)),
                ('band2', models.CharField(blank=True, max_length=255, null=True)),
                ('band3', models.CharField(blank=True, max_length=255, null=True)),
                ('band4', models.CharField(blank=True, max_length=255, null=True)),
                ('band5', models.CharField(blank=True, max_length=255, null=True)),
                ('offentliggjort', models.BooleanField()),
                ('spillested', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.spillested')),
            ],
            options={
                'verbose_name_plural': 'Koncerter',
            },
        ),
    ]
