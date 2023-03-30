# Generated by Django 4.1.7 on 2023-03-21 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='category')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Categories',
                'verbose_name_plural': 'Categories',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True)),
                ('specif', models.TextField()),
                ('photo', models.ImageField(upload_to='photos/%Y/%/m/%d/')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('link_p', models.CharField(max_length=255, null=True)),
                ('price_p', models.FloatField(null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category')),
            ],
            options={
                'verbose_name': 'Techno site',
                'verbose_name_plural': 'Techno site',
                'ordering': ['time_create', 'title'],
            },
        ),
    ]