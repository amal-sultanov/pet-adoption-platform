# Generated by Django 5.1.4 on 2024-12-24 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsCategoryModel',
            new_name='PostCategoryModel',
        ),
    ]
