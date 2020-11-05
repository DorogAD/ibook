from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Book, Category, Genre, Owner
from django.db.models import F
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, BookForm, EmailBookForm  # , AddBookModelForm
from django.contrib.auth import login, logout
import datetime


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
    model = Book# это значит моделью будет именно эта модель из файла моделей
    template_name = 'bookz/single.html'
    context_object_name = 'book'# здесь мы вручную задаем имя переменной контекста для лучшей читабельности

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1# класс Ф нужен для обновления количества просмотров.
        # мы обращаемся к атрибуту вьюс объекта бук и добавляем к имеющемуся там значению еще один просмотр
        self.object.save()# метод сэйв сохраняет количество просмотров
        self.object.refresh_from_db()# перезапрашиваем данные из базы данных после сохранения
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


class BooksByOwners(ListView):
    template_name = 'bookz/index.html'
    context_object_name = 'books'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Book.objects.filter(owner__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Книги по автору: ' + str(Owner.objects.get(slug=self.kwargs['slug']))
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

        if form.is_valid():
            print('valid')#проверка валидности, ок
            print(form.cleaned_data)#проверка что внутри, выдает все то что вводится в форму
            print(request.user.email)#проверка выдается ли имейл, ок

            book_entry = Book()
            book_entry.title = form.cleaned_data['title']
            book_entry.author = form.cleaned_data['author']
            book_entry.content = form.cleaned_data['content']
            book_entry.created_at = datetime.datetime.now()#ошибка исправилась когда поменял from datetime import datetime на import datetime
            book_entry.photo = form.cleaned_data['photo']
            book_entry.owner = Owner.objects.get(email=request.user.email)# выдает ошибку: Field 'id' expected a number but got 'sa_do@tut.by'
            #book_entry.owner = get_object_or_404(Owner, pk=Owner.email)# выдает ошибку: Owner matching query does not exist
            book_entry.category = form.cleaned_data['category']
            book_entry.genres = form.cleaned_data['genres']
            book_entry.town = form.cleaned_data['town']
            book_entry.type = form.cleaned_data['type']

            book_entry.save()
            #book_entry.genres.add(request.genres)
            #Book.objects.create(**form.cleaned_data)
            return redirect('/home/')
        print('invalid')
        print(form.cleaned_data)

    else:
        form = BookForm()
        return render(request, 'newbook.html', {'form': form})
        print()



#создаю функцию чтобы выводить список жанров на отдельной странице
def genres_all(request):
    all_genres = Genre.objects.all()

    return render(request, 'genres_new.html', {'all_genres': all_genres})

#создаю функцию чтобы выводить список книг на отдельной странице
def books_all(request):
    all_books = Book.objects.all()

    return render(request, 'find_book.html', {'all_books': all_books})


#создаю функцию чтобы выводить список популярных книг на отдельной странице
def popular(request):
    books = Book.objects.order_by('-views')[:4]
    return render(request, 'popular.html', {"books": books})

#создаю функцию чтобы выводить список недавно добавленных книг на отдельной странице
def novinki(request):
    books = Book.objects.order_by('-created_at')[:4]
    return render(request, 'novinki.html', {"books": books})

#создаю функцию чтобы выводить страницу о сайте
def about(request):
    #pass
    #books = Book.objects.order_by('-created_at')[:4]
    return render(request, 'about.html')

'''
#представление обмена электронными сообщениями посредством почты
def book_share(request, book_id):
    # Получить пост по id
    book = get_object_or_404(Book, id=book_id, status='published')
    sent = False
    if request.method == 'POST':
        # Форма была отправлена
        form = EmailBookForm(request.POST)
        if form.is_valid():
            # Поля формы прошли проверку
	        cd = form.cleaned_data
            book_url = request.build_absolute_url(book.get_absolute_url())
            subject = '{} ({}) recommends you reading " {}"'.format(cd['name'], cd['email'], book.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(book.title, book_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
            # ... отправить письмо
    else:
        form = EmailBookForm()
    return render(request, '/bookz/share.html', {'book': book, 'form': form})
'''
