from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Book, Category, Genre
from django.db.models import F
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, BookForm  # , AddBookModelForm
from django.contrib.auth import login, logout
from datetime import datetime


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'bookz/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'bookz/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')





class Home(ListView):
    model = Book
    template_name = 'bookz/index.html'
    context_object_name = 'books'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Book Design'
        return context


class BooksByCategory(ListView):
    template_name = 'bookz/index.html'
    context_object_name = 'books'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Book.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class GetBook(DetailView):
    model = Book
    template_name = 'bookz/single.html'
    context_object_name = 'book'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class BooksByGenre(ListView):
    template_name = 'bookz/index.html'
    context_object_name = 'books'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Book.objects.filter(genres__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Книги по жанру: ' + str(Genre.objects.get(slug=self.kwargs['slug']))
        return context


class Search(ListView):
    template_name = 'bookz/search.html'
    context_object_name = 'books'
    paginate_by = 4

    def get_queryset(self):
        return Book.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context

def newbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
    else:
        form = BookForm()
        return render(request, 'newbook.html', {'form': form})

'''
def add_book(request):

    if request.method == "POST":

        form = AddBookModelForm(request.POST, request.FILES) #or AddPost

        if form.is_valid():

            book_entry = Book()
            book_entry.author = form.cleaned_data['author']
            book_entry.issued = datetime.datetime.now()
            book_entry.title = form.cleaned_data['title']
            book_entry.subtitle = form.cleaned_data['subtitle']
            book_entry.photo = form.cleaned_data['photo']
            book_entry.type = form.cleaned_data['type']
            book_entry.content = form.cleaned_data['content']

            book_entry.save()
            return redirect('/home/')

    form = AddBookModelForm() #or AddPost
    return render(request, 'add_book_old.html', {'form': form})

'''