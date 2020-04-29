# Generated by Django 3.0.3 on 2020-04-16 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('material', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('img_url', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Treasure',
        ),
    ]
