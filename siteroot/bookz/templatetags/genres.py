from django import template
from bookz.models import Genre

register = template.Library()

@register.inclusion_tag('bookz/genres_tpl.html')
def get_genres():
    genres = Genre.objects.all()
    return {"genres": genres}