# Generated by Django 4.1 on 2022-09-04 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_rename_scope_scopes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Scopes',
            new_name='Scope',
        ),
    ]
