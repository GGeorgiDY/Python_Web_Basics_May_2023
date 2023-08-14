from datetime import datetime
from django.template import Library

register = Library()


@register.filter('odd')  # така с 'odd' му даваме име
def odd(values):
    return [x for x in values if x % 2 == 1]


@register.filter('app_style')
def format_to_app_style(date):
    return date.strftime('%Y/%m/%d %H:%M')