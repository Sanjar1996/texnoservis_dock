# Generated by Django 3.2.8 on 2021-10-21 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20211020_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricingplan',
            name='price',
        ),
        migrations.AddField(
            model_name='pricingplan',
            name='file',
            field=models.FileField(blank=True, upload_to='files/'),
        ),
    ]