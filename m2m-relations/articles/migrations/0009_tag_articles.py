# Generated by Django 4.1 on 2022-09-04 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_scope_is_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(through='articles.Scope', to='articles.article'),
        ),
    ]
