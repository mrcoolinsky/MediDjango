from django import template

register = template.Library()


@register.filter(name='is_receptionist')
def is_receptionist(user):
    return user.groups.filter(name='Recepcjonista').exists()


@register.filter(name='is_doctor')
def is_doctor(user):
    return user.groups.filter(name='Lekarz').exists()


@register.filter(name='is_patient')
def is_doctor(user):
    return user.groups.filter(name='Pacjent').exists()


@register.filter
def get_range(value):
    return range(value)

