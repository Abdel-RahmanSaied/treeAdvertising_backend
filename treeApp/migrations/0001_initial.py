# Generated by Django 4.0.3 on 2022-05-28 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client_level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(choices=[('R', 'Red'), ('G', 'Green'), ('B', 'Blue')], default='B', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('clientlevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treeApp.client_level')),
            ],
        ),
    ]
