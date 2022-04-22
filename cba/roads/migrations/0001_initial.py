# Generated by Django 2.1.2 on 2018-10-16 19:04

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('road_section_id', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='road section id')),
                ('road_number', models.SmallIntegerField(verbose_name='road number')),
                ('road_name', models.CharField(max_length=255, verbose_name='road name')),
                ('road_start', models.CharField(max_length=255, verbose_name='road start')),
                ('road_end', models.CharField(max_length=255, verbose_name='road end')),
                ('section_order', models.SmallIntegerField(null=True, verbose_name='section order')),
                ('section_name', models.CharField(max_length=255, verbose_name='section name')),
            ],
            options={
                'verbose_name': 'section',
                'verbose_name_plural': 'sections',
                'ordering': ('road_section_id',),
            },
        ),
    ]