# Generated by Django 4.2.16 on 2024-12-03 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='copy',
            new_name='text',
        ),
    ]
