# Generated by Django 2.1.7 on 2019-04-17 15:21

from django.db import migrations, models
import inventory.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('category_id', models.PositiveIntegerField()),
                ('provider_id', models.PositiveIntegerField()),
            ],
            managers=[
                ('objects', inventory.models.ItemManager()),
            ],
        ),
    ]
