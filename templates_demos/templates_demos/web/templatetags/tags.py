from django.template import Library

from templates_demos.web.views import Student

register = Library()


# simple tag example
@register.simple_tag(name='student_info')
def show_student_info(student: Student):
    return f'Hello, My name is {student.name} and my age is {student.age}'


@register.simple_tag(name='sample_tag')
def simple_tag(*args, **kwargs):
    return ', '.join(str(x) for x in (list(args) + list(kwargs.items())))


@register.inclusion_tag('tags/nav.html', name='app_nav')
def generate_nav(*args):
    context = {
        'url_names': args,
    }
    return context