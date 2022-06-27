# Generated by Django 4.0.5 on 2022-06-27 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accommodations', '0010_alter_accommodationaward_accommodation_and_more'),
        ('review', '0009_alter_review_cooperation_syndication_partner_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='accommodation',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='accommodations.accommodation'),
            preserve_default=False,
        ),
    ]