from django import template
from django.utils.safestring import mark_safe

register = template.Library()

TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """
TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """
PRODUCT_SPEC = {
    'clothes': {
        'Model': 'model',
        'Gen': 'gender',
        'Sezon': 'season',
        'Stil': 'style',
        'Mărime': 'size',
        'Culoare': 'color'
    },
    'shoes': {
        'Model': 'model',
        'Gen': 'gender',
        'Sezon': 'season',
        'Mărime': 'size',
        'Culoare': 'color'

    },
    'accessories': {
        'Gen': 'gender',
        'Culoare': 'color'

    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
