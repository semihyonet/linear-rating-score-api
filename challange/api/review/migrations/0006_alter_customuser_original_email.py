# Generated by Django 4.0.5 on 2022-06-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_alter_customuser_original_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='original_email',
            field=models.EmailField(default='', max_length=256, null=True),
        ),
    ]
