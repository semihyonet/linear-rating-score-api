# Generated by Django 4.0.5 on 2022-06-25 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_date', models.DateTimeField()),
                ('locale', models.CharField(max_length=8)),
                ('location_review', models.SmallIntegerField(null=True)),
                ('service_review', models.SmallIntegerField(null=True)),
                ('priceQuality_review', models.SmallIntegerField(null=True)),
                ('food_review', models.SmallIntegerField(null=True)),
                ('room_review', models.SmallIntegerField(null=True)),
                ('childFriendly_review', models.SmallIntegerField(null=True)),
                ('interior_review', models.SmallIntegerField(null=True)),
                ('size_review', models.SmallIntegerField(null=True)),
                ('activities_review', models.SmallIntegerField(null=True)),
                ('restaurants_review', models.SmallIntegerField(null=True)),
                ('sanitaryState_review', models.SmallIntegerField(null=True)),
                ('accessibility_review', models.SmallIntegerField(null=True)),
                ('nightlife_review', models.SmallIntegerField(null=True)),
                ('culture_review', models.SmallIntegerField(null=True)),
                ('surrounding_review', models.SmallIntegerField(null=True)),
                ('atmosphere_review', models.SmallIntegerField(null=True)),
                ('noviceSkiArea_review', models.SmallIntegerField(null=True)),
                ('advancedSkiArea_review', models.SmallIntegerField(null=True)),
                ('apresSki_review', models.SmallIntegerField(null=True)),
                ('beach_review', models.SmallIntegerField(null=True)),
                ('entertainment_review', models.SmallIntegerField(null=True)),
                ('environmental_review', models.SmallIntegerField(null=True)),
                ('pool_review', models.SmallIntegerField(null=True)),
                ('terrace_review', models.SmallIntegerField(null=True)),
                ('housing_review', models.SmallIntegerField(null=True)),
                ('hygiene_review', models.SmallIntegerField(null=True)),
                ('traveled_with', models.CharField(max_length=31)),
                ('cooperation_import_partner', models.CharField(max_length=31)),
                ('cooperation_syndication_partner_id', models.CharField(max_length=31)),
                ('entry_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ref', models.CharField(max_length=32)),
                ('original_name', models.CharField(max_length=64)),
                ('original_email', models.EmailField(max_length=254, verbose_name=64)),
                ('original_ip', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('language', models.CharField(max_length=8)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.review')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('language', models.CharField(max_length=8)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.review')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.user'),
        ),
    ]
