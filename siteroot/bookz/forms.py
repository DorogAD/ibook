from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Genre, Town, Type



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class BookForm(forms.Form):

    title = forms.CharField(max_length=255, label='Название книги')
    author = forms.CharField(max_length=100, label='Автор книги')
    content = forms.CharField(label='Аннотация', widget=forms.Textarea)
    #genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), label='Жанры', widget=forms.Select)
    #photo = forms.ImageField(label='Фото обложки')
    #town = forms.ModelChoiceField(queryset=Town.objects.all(), label='Город', widget=forms.Select)
    #type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Вариант', widget=forms.Select)

