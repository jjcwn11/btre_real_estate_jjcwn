# Generated by Django 3.1.2 on 2020-10-13 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20201013_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(),
        ),
    ]
