# Generated by Django 3.0.3 on 2020-04-16 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generalapp', '0002_auto_20200416_0001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='material',
            new_name='type',
        ),
    ]