from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Genre, Town, Type, Category


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
    #slug = forms.SlugField(max_length=100, label='url')
    author = forms.CharField(max_length=100, label='Автор книги')
    content = forms.CharField(label='Аннотация', widget=forms.Textarea)
    photo = forms.ImageField(label='Фото обложки')
    genres = forms.ModelChoiceField(queryset=Genre.objects.all(), label='Жанры', widget=forms.Select)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория')
    town = forms.ModelChoiceField(queryset=Town.objects.all(), label='Город', widget=forms.Select)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Вариант', widget=forms.Select)





#добавляем форму обмена комментариями по имейл
class EmailBookForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

