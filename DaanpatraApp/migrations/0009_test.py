# Generated by Django 3.1.5 on 2021-01-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DaanpatraApp', '0008_auto_20210113_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='Test')),
            ],
        ),
    ]
