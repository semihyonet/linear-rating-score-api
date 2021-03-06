# Generated by Django 4.0.5 on 2022-06-27 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accommodations', '0009_alter_helioshistoricalurl_new_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodationaward',
            name='accommodation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accommodation_awards', to='accommodations.accommodation'),
        ),
        migrations.AlterField(
            model_name='accommodationfacility',
            name='accommodation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accommodation_facility', to='accommodations.accommodation'),
        ),
        migrations.AlterField(
            model_name='accommodationnames',
            name='accommodation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accommodation_names', to='accommodations.accommodation'),
        ),
        migrations.AlterField(
            model_name='accommodationparents',
            name='accommodation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accommodation_parents', to='accommodations.accommodation'),
        ),
        migrations.AlterField(
            model_name='helioshistoricalurl',
            name='accommodation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accommodation_helios_historical_url', to='accommodations.accommodation'),
        ),
    ]
