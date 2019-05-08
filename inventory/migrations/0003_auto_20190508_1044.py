# Generated by Django 2.2 on 2019-05-08 16:44

import datetime
from django.db import migrations, models
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20190501_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            managers=[
                ('objects', inventory.models.DocumentManager()),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_id', models.PositiveIntegerField()),
                ('item_id', models.PositiveIntegerField()),
                ('quantity_in', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            managers=[
                ('objects', inventory.models.GenericManager()),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='lead_time',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='reorder_point',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]