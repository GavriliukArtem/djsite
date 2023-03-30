from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class ShopHome(DataMixin, ListView):
    """The class is List of all goods on the site
    DataMixin use for to create maine menu for this and another pages"""
    model = Shop
    template_name = 'shop/index.html'
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, **kwargs):
        """A standard function for format content"""
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Main page')
        return dict(list(c_def.items()) + list(context.items()))

    def get_queryset(self):
        """Filter for check a good is published or not"""
        return Shop.objects.filter(is_published=True).select_related('cat')


class Search(DataMixin, ListView):
    """Search"""
    template_name = 'shop/index.html'
    paginate_by = 4
    context_object_name = 'goods'

    def get_queryset(self):
        """Filter use with standard library django.Q
        search in title and content with 'icontains'"""
        return Shop.objects.filter(
            Q(title__icontains=self.request.GET.get('q')) | Q(content__icontains=self.request.GET.get('q')))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Search page')
        context['q'] = self.request.GET.get('q')
        return dict(list(c_def.items()) + list(context.items()))


def about(request):
    """Information about site"""
    return render(request, 'shop/about.html', {'menu': menu, 'title': 'About site.'})


class AddGoods(LoginRequiredMixin, DataMixin, CreateView):
    """The class is for add goods use a standard class CreateView
    and a standard LoginRequriredMixin for check authenticated user or not"""
    form_class = AddGoodsForm
    template_name = 'shop/addgoods.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add goods')
        return dict(list(c_def.items()) + list(context.items()))


class ContactFormView(DataMixin, FormView):
    """The class for feedback, used a standard form"""
    form_class = ContactForm
    template_name = 'shop/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Feedback')
        return dict(list(c_def.items()) + list(context.items()))

    def form_valid(self, form):
        """Validation check and redirect to home"""
        print(form.cleaned_data)
        return redirect('home')


class ShowProduct(DataMixin, DetailView):
    """Details about the product, shows all information about the product"""
    model = Shop
    template_name = 'shop/product.html'
    slug_url_kwarg = 'prd_slug'
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['goods'])
        return dict(list(c_def.items()) + list(context.items()))


class ShopCategory(DataMixin, ListView):
    """All categories used to display """
    model = Shop
    template_name = 'shop/index.html'
    context_object_name = 'goods'
    allow_empty = False  # if empty don't show a category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Category' + ': ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(c_def.items()) + list(context.items()))

    def get_queryset(self):
        """Filter for in slug of cat"""
        return Shop.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


class RegisterUser(DataMixin, CreateView):
    """Class for to register users"""
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Registration')
        return dict(list(c_def.items()) + list(context.items()))

    def form_valid(self, form):
        """Validation"""
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    """The class for login registered users"""
    form_class = LoginUserForm
    template_name = 'shop/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='LOGIN')
        return dict(list(c_def.items()) + list(context.items()))

    def get_success_url(self):
        """if valid to redirect"""
        return reverse_lazy('home')


class UpdateGoods(DataMixin, UpdateView):
    """Update goods with a standard class 'UpdateView'"""
    model = Shop
    template_name = 'shop/addgoods.html'
    form_class = AddGoodsForm
    slug_url_kwarg = 'prd_slug'
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['goods'])
        return dict(list(c_def.items()) + list(context.items()))


class DeleteGoods(DataMixin, DeleteView):
    """Delete goods with a standard class 'DeleteView'"""
    model = Shop
    template_name = 'shop/deletegoods.html'
    slug_url_kwarg = 'prd_slug'
    context_object_name = 'goods'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['goods'])
        return dict(list(c_def.items()) + list(context.items()))


def logout_user(request):
    """Logout users"""
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found. Sorry((</h1>')
