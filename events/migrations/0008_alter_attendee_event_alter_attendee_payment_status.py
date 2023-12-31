# Generated by Django 5.0 on 2023-12-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_rename_attendeee_attendee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='event',
            field=models.ManyToManyField(to='events.event'),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='payment_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]