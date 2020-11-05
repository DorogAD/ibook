from django import template
from bookz.models import Genre, Book

register = template.Library()

@register.inclusion_tag('bookz/genres_tpl.html')
def get_genres():
    #genres = Genre.objects.all()
    genres = Book.genres.objects.all()
    real_genres = []
    for genre in genres:
        if genre in Book.genres:
            real_genres.append(genre)
        return real_genres
    return {"genres": real_genres}

''' старый рабочий вариант
@register.inclusion_tag('bookz/genres_tpl.html')
def get_genres():
    genres = Genre.objects.all()
    return {"genres": genres}
'''