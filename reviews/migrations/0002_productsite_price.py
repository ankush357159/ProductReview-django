# Generated by Django 4.0.1 on 2022-01-13 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsite',
            name='price',
            field=models.DecimalField(decimal_places=2, default=35000, max_digits=9),
            preserve_default=False,
        ),
    ]
