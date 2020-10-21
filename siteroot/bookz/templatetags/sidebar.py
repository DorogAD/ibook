from django import template
from bookz.models import Book, Genre

register = template.Library()

@register.inclusion_tag('bookz/popular_books_tpl.html')
def get_popular(cnt):
    books = Book.objects.order_by('-views')[:cnt]
    return {"books": books}

@register.inclusion_tag('bookz/genres_tpl.html')
def get_genres():
    genres = Genre.objects.all()
    return {"genres": genres}
