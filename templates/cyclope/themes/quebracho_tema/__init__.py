# *-- coding:utf-8 --*
"""Configuration for the Neutrona theme templates and regions.

Attributes:
    verbose_name: name of theme to be displayed in the admin interface
    layout_templates: dictionary defining regions for the available templates
"""

from django.utils.translation import ugettext_lazy as _

verbose_name = 'Tema Quebracho'

layout_templates = {

    '4_elements.html':
        {
        'verbose_name': _('4 Elements'),
        'regions' : {
            'air': _('air'),
            'water': _('water'),
            'before_fire': _('before fire'),
            'after_fire': _('after fire'),
            'earth': _('earth'),
            }
        },

    '5_elements.html':
        {
        'verbose_name': _('5 Elements'),
        'regions' : {
            'air': _('air'),
            'water': _('water'),
            'love': _('love'),
            'before_fire': _('before fire'),
            'after_fire': _('after fire'),
            'earth': _('earth'),
            }
        },
    'barra_lateral.html':
        {
        'verbose_name': 'Barra lateral',
        'regions' : {
            'air': _('air'),
            'water': _('water'),
            'love': _('love'),
            'before_fire': _('before fire'),
            'after_fire': _('after fire'),
            'earth': _('earth'),
            }
        },
    'pagina_completa.html':
        {
        'verbose_name': 'Página completa',
        'regions' : {
            'air': _('air'),
            'water': _('water'),
            'love': _('love'),
            'before_fire': _('before fire'),
            'after_fire': _('after fire'),
            'earth': _('earth'),
            }
        },
    'home_arbol.html':
        {'verbose_name': 'Inicio',
         'regions': {}
         },
    'empty.html':
        {'verbose_name': _('Empty'),
         'regions': {}
         },

    'newsletter.html':
        {'verbose_name': _('Newsletter'),
        'regions' : {
            'header': _('header'),
            'before_content': _('before content'),
            'after_content': _('after content'),
            }
         },
}
