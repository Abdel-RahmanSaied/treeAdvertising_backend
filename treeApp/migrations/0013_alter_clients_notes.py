# Generated by Django 4.0.3 on 2022-05-31 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treeApp', '0012_alter_orders_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='notes',
            field=models.CharField(default='', max_length=255),
        ),
    ]
