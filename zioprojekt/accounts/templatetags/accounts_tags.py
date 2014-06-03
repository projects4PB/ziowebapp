from django import template
register = template.Library()


@register.filter
def is_participant(instance, arg):
    return instance.is_participant(arg)


@register.filter
def is_moderator(instance, arg):
    return instance.is_moderator(arg)
