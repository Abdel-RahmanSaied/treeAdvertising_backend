# Generated by Django 4.0.3 on 2022-05-31 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treeApp', '0013_alter_clients_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='notes',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
