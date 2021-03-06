# Generated by Django 3.1.5 on 2021-01-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DaanpatraApp', '0025_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='donation_status',
            field=models.BooleanField(blank=True, help_text='Check when delivery get successful.', null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='product_category',
            field=models.CharField(choices=[('clothes', 'Clothes'), ('food', 'Food'), ('utensils', 'Utensils'), ('equipments', 'Equipments'), ('books', 'Books'), ('medicines', 'Un-Expired Medicines'), ('other', 'Other')], max_length=30),
        ),
    ]
