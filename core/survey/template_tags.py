from django import template

register= template.Library()

@register.filter
def get_value(obj, field):
    """
        Obtiene el valor de un objeto o diccionario, Soporta notacion ORM obj__field
    """

    if field is None or obj is None:
        return ''
    try:
        objects = field.split('__')
        if len(objects) > 0:
            row=obj
            for r in row:
                value = getattr(row, r)
                row = value
        else:
            value = getattr(obj, field)
        
        return value
    except AttributeError:
        try:
            return obj[field]
        except:
            return ''
    except:
        return ''


