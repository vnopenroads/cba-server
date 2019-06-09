# Generated by Django 2.2.2 on 2019-06-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0005_auto_20190607_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='aadt_4wheel',
            field=models.FloatField(blank=True, null=True, verbose_name='aadt_4wheel'),
        ),
        migrations.AddField(
            model_name='section',
            name='aadt_articulatedtruck',
            field=models.FloatField(blank=True, null=True, verbose_name='aadt_articulatedtruck'),
        ),
        migrations.AddField(
            model_name='section',
            name='aadt_carmedium',
            field=models.FloatField(blank=True, null=True, verbose_name='aadt_carmedium'),
        ),
        migrations.AddField(
            model_name='section',
            name='aadt_carsmall',
            field=models.FloatField(blank=True, null=True, verbose_name='aadt_carsmall'),
        ),
        migrations.AddField(
            model_name='section',
            name='aadt_delivery',
            field=models.FloatField(blank=True, null=True, verbose_name='aadt_delivery'),
        ),
        migrations.AddField(
            model_name='section',
            name='aadt_largebus',
            field=models.FloatField(blank=True, null=True, verbose_name='aadt_largebus'),
        ),
        migrations.AddField(
            model_name='section',
            name='aadt_largetruck',
            field=models.FloatField(blank=True, null=True, verbose_name='aadt_largetruck'),
        ),
        migrations.AddField(
            model_name='section',
            name='aadt_mediumbus',
            field=models.FloatField(blank=True, null=True, verbose_name='aadt_mediumbus'),
        ),
        migrations.AddField(
            model_name='section',
            name='aadt_mediumtruck',
            field=models.FloatField(blank=True, null=True, verbose_name='aadt_mediumtruck'),
        ),
        migrations.AddField(
            model_name='section',
            name='aadt_motorcyle',
            field=models.FloatField(blank=True, null=True, verbose_name='aadt_motorcyle'),
        ),
        migrations.AddField(
            model_name='section',
            name='aadt_smallbus',
            field=models.FloatField(blank=True, null=True, verbose_name='aadt_smallbus'),
        ),
        migrations.AddField(
            model_name='section',
            name='aadt_smalltruck',
            field=models.FloatField(blank=True, null=True, verbose_name='aadt_smalltruck'),
        ),
        migrations.AddField(
            model_name='section',
            name='aadt_total',
            field=models.FloatField(blank=True, null=True, verbose_name='aadt_total'),
        ),
        migrations.AddField(
            model_name='section',
            name='pavement_age',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='pavement age'),
        ),
        migrations.AddField(
            model_name='section',
            name='structural_no',
            field=models.FloatField(blank=True, null=True, verbose_name='structural number'),
        ),
    ]
