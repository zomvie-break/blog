from django import template

register =  template.Library()

@register.simple_tag
def active(request_path, target_path):
    """
    A simple tag used in the navbar to set list items' classes to active so that they are highlited if active.
    """
    if str(request_path) == str(target_path): 
        return 'active'
    return ''
