# Generated by Django 5.1.4 on 2025-01-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_adoptionmodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionmodel',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
