# Generated by Django 4.1.7 on 2023-03-21 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='content',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='shop',
            name='specif',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]