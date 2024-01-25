# Generated by Django 5.0.1 on 2024-01-24 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Villa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('capacity', models.IntegerField()),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
