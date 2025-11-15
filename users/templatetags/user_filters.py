from django import template

register = template.Library()

@register.filter
def is_editor(user):
    return user.groups.filter(name="Editor").exists()
