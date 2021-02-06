# Generated by Django 3.1.5 on 2021-02-06 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DaanpatraApp', '0028_donationgallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('can_add_sub_admin', 'Access to add Sub Admin'), ('can_update_sub_admin', 'Access to update Sub Admin'), ('can_remove_sub_admin', 'Access to remove Sub Admin'), ('can_add_drivers', 'Access to add Drivers'), ('can_remove_drivers', 'Access to remove Drivers'), ('can_update_drivers', 'Access to update Drivers'), ('can_add_location', 'Access to add location'), ('can_remove_location', 'Access to remove location'), ('can_update_location', 'Access to update location'), ('can_update_donation_status', 'Access to update Donation Status'), ('can_add_donation_gallery_images', 'Access to Add Donation Gallery Images'), ('can_remove_donation_gallery_images', 'Access to Delete Donation Gallery Images'))},
        ),
    ]
