# Generated by Django 2.2.2 on 2019-06-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0004_managementclass_moistureclass_pavementconditionclass_pavementtype_roadclass_surfacetype_temperaturec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='road_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='road number'),
        ),
    ]