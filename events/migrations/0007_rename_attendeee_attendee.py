# Generated by Django 5.0 on 2023-12-30 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_attendeee_delete_creator'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attendeee',
            new_name='Attendee',
        ),
    ]
