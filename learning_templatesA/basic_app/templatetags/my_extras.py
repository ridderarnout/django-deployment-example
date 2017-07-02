from django import template

register = template.Library()

def cut(value,arg):
    """
    This cuts out all values of "agr" from the string!
    """
    return value.replace(arg,'')

register.filter('cut', cut)
