from django import template

register = template.Library()

@register.simple_tag
def get_range(num):
    return range(1, num+1)
