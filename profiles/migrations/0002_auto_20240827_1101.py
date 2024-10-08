# Generated by Django 3.0 on 2024-08-27 09:01

from django.db import migrations


def copy_profiles_data(apps, schema_editor):
    old_profiles = apps.get_model('oc_lettings_site', 'Profile')
    new_profiles = apps.get_model('profiles', 'Profile')

    for old_profile in old_profiles.objects.all():
        new_profiles.objects.create(
            user=old_profile.user,
            favorite_city=old_profile.favorite_city,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_profiles_data),
    ]
