from django import template

register = template.Library()


@register.filter(name='slice')
def slice(value):
    return value[0:300]