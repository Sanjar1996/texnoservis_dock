# Generated by Django 3.2.8 on 2021-10-20 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_dockmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qaror',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=45)),
                ('title', models.CharField(max_length=150)),
                ('sub_title', models.CharField(max_length=450)),
                ('body', models.TextField()),
            ],
        ),
    ]
