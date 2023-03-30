from django.db import models
from django.urls import reverse


class Shop(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name="Content")
    specif = models.TextField(max_length=500, null=True, blank=True, verbose_name='Specification')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Photo")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    link_p = models.CharField(max_length=255, null=True, verbose_name="Link")
    price_p = models.FloatField(null=True, verbose_name="Price")
    is_published = models.BooleanField(default=True, verbose_name="Publish")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Category")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ditail', kwargs={'prd_slug': self.slug})

    def get_absolute_url_update(self):
        return reverse('update', kwargs={'prd_slug': self.slug})

    class Meta:
        verbose_name = 'Techno site'
        verbose_name_plural = 'Techno site'
        ordering = ['time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='category')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'
        ordering = ['id']  # sort category in 'id'
