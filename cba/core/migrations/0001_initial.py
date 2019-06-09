# Generated by Django 2.2.2 on 2019-06-08 04:56

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CBAResult',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('work_class', models.CharField(blank=True, max_length=100, verbose_name='work class')),
                ('work_type', models.CharField(blank=True, max_length=100, verbose_name='work type')),
                ('work_name', models.CharField(blank=True, max_length=100, verbose_name='work name')),
                ('work_cost', models.FloatField(blank=True, null=True, verbose_name='financial cost')),
                ('work_cost_km', models.FloatField(blank=True, null=True, verbose_name='financial cost per km')),
                ('work_year', models.SmallIntegerField(blank=True, null=True, verbose_name='implementation year')),
                ('npv', models.FloatField(blank=True, null=True, verbose_name='npv')),
                ('npv_km', models.FloatField(blank=True, null=True, verbose_name='npv per km')),
                ('npv_cost', models.FloatField(blank=True, null=True, verbose_name='npv per road work cost')),
                ('eirr', models.FloatField(blank=True, null=True, verbose_name='eirr')),
                ('aadt', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), size=10)),
                ('iri_projection', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), size=10)),
                ('iri_base', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), size=10)),
                ('con_projection', django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(blank=True, null=True), size=10)),
                ('con_base', django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(blank=True, null=True), size=10)),
                ('financial_recurrent_cost', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), size=10)),
                ('net_benefits', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), size=20)),
            ],
            options={
                'verbose_name': 'cost benefit analysis result',
            },
        ),
    ]
