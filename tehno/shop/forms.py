from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *


class AddGoodsForm(forms.ModelForm):
    """A Form for to add goods"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Empty'

    class Meta:
        """Style for forms and fields which used in the form"""
        model = Shop
        fields = ['title', 'slug', 'content', 'specif', 'photo', 'cat', 'price_p', 'is_published', 'link_p']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_data(self):
        """Validation"""
        title = self.cleaned_data['title']
        if len(title) > 240:
            raise ValidationError("Title can't be more 200 symbols")

        return title


class RegisterUserForm(UserCreationForm):
    """The class for register users with use a standard form 'UserCreationForm'
    and use style for field with tool widget"""
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        """Fields for input"""
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    """The class for the login users which already registered.
    Use a standard class 'AuthenticationForm'"""
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    """Form for to send feedback"""
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()
