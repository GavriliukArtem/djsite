from django import template
from shop.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(fiter=None):
    if not fiter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=fiter)


@register.inclusion_tag('shop/list_category.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}
