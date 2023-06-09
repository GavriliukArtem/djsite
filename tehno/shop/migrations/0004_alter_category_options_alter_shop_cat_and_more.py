# Generated by Django 4.1.7 on 2023-03-27 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_category_options_alter_shop_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Categories', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='shop',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='content',
            field=models.TextField(blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Publish'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='link_p',
            field=models.CharField(max_length=255, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='price_p',
            field=models.FloatField(null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='specif',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Specification'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]
