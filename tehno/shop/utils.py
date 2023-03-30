from django.db.models import Count
from .models import *

menu = [{'title': 'About site', 'url_name': 'about'},
        {'title': 'Add goods', 'url_name': 'add_goods'},
        {'title': 'Feedback', 'url_name': 'contact'},
        ]


class DataMixin:
    """ Mixin for to create maine menu for site"""
    paginate_by = 4

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('shop'))
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
