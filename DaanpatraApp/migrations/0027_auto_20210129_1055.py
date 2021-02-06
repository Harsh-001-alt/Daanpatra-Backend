# Generated by Django 3.1.5 on 2021-01-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DaanpatraApp', '0026_auto_20210129_0551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('can_add_sub_admin', 'Access to add Sub Admin'), ('can_update_sub_admin', 'Access to update Sub Admin'), ('can_remove_sub_admin', 'Access to remove Sub Admin'), ('can_add_drivers', 'Access to add Drivers'), ('can_remove_drivers', 'Access to remove Drivers'), ('can_update_drivers', 'Access to update Drivers'), ('can_add_location', 'Access to add location'), ('can_remove_location', 'Access to remove location'), ('can_update_location', 'Access to update location'), ('can_update_donation_status', 'Access to update Donation Status'))},
        ),
        migrations.AlterField(
            model_name='donation',
            name='donation_status',
            field=models.BooleanField(default=False, help_text='Check when delivery gets successful.'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='product_category',
            field=models.CharField(choices=[('clothes', 'Clothes'), ('food', 'Raw Food'), ('utensils', 'Utensils'), ('equipments', 'Equipments'), ('books', 'Books'), ('medicines', 'Un-Expired Medicines'), ('other', 'Other')], max_length=30),
        ),
    ]