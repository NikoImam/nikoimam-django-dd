from django import forms
from django.contrib.auth import get_user_model
from web.models import *

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Адрес эл.почты')
    username = forms.CharField(label='Логин')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    repeat_password = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль')
    field_order = ["first_name", "last_name", "email", "username", "password", "repeat_password"]

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['repeat_password']:
            self.add_error('password', 'Пароли не совпадают')
        return cleaned_data

    class Meta:
        model = User
        fields = {"first_name", "last_name", "email", "username", "password", "repeat_password"}


class AuthForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок')
    text = forms.CharField(widget=forms.Textarea(), label='Содержимое')

    class Meta:
        model = Post
        fields = ('title', 'text')


class CarForm(forms.ModelForm):
    year = forms.IntegerField(label='Год производства')

    def save(self, commit=True):
        self.instance.owner = self.initial['user']
        return super().save(commit)

    class Meta:
        model = Car
        fields = ('model', 'year', 'image')

