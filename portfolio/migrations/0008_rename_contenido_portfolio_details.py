# Generated by Django 3.2.4 on 2021-06-26 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20210626_0349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='contenido',
            new_name='details',
        ),
    ]
