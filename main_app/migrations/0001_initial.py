# Generated by Django 4.0.3 on 2022-03-12 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('hex_value', models.CharField(blank=True, max_length=7, null=True)),
                ('colour_name', models.CharField(blank=True, max_length=150, null=True)),
                ('color_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'color',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('brand', models.CharField(max_length=150)),
                ('product_name', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=65535, max_digits=65535)),
                ('website_link', models.CharField(max_length=150)),
                ('tags', models.CharField(max_length=150)),
                ('image_link', models.CharField(max_length=1000)),
                ('product_description', models.CharField(max_length=4000)),
                ('product_type', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
    ]
