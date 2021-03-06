# Generated by Django 2.2 on 2019-05-13 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20190508_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='document_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Document'),
        ),
        migrations.AlterField(
            model_name='movement',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item'),
        ),
    ]
