
from django import template
from ..models import Book, Mulu

register = template.Library()

@register.simple_tag
def get_recent_books(num=5):
	return Book.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_mulus():
	return Mulu.objects.all()