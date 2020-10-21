from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book

from bookz.models import Book


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class BookForm(forms.Form):

    title = forms.CharField(max_length=255, label='title')
    content = forms.CharField(label='content')
    #genre = forms.ModelChoiceField(queryset=Book.genres.all())


'''
class AddBookModelForm(forms.ModelForm):

    class Meta:

        model = Book
        fields = ('title', 'author', 'content', 'type', 'photo')
        labels = {'photo': 'Book photo'}
'''