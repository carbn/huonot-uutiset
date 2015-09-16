from django import template

register = template.Library()

# from http://stackoverflow.com/questions/19268727/django-how-to-get-the-name-of-the-template-being-rendered
@register.simple_tag
def active_page(request, view_name):
    from django.core.urlresolvers import resolve, Resolver404
    if not request:
        return ""
    try:
        return "active" if resolve(request.path_info).url_name == view_name else ""
    except Resolver404:
        return ""
