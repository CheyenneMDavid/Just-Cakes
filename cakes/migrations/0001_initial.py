# Generated by Django 3.2.20 on 2023-09-06 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CakeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Flavour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavour', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_gluten_free', models.BooleanField()),
                ('is_plant_based', models.BooleanField()),
                ('number_of_layers', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('flavours', models.ManyToManyField(to='cakes.Flavour')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakes.caketype')),
            ],
        ),
    ]