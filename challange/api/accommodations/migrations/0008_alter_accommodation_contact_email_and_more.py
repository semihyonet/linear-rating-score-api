# Generated by Django 4.0.5 on 2022-06-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodations', '0007_alter_accommodation_address_street_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='contact_email',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='contact_url',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='fallback_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='accommodationfacility',
            name='id_ref',
            field=models.CharField(max_length=128),
        ),
    ]