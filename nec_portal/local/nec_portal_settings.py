from django.utils.translation import ugettext_lazy as _

# Admin links list.
# NOTE: If you want to add an external link,
# please add the specified name description and url.
#   name: Specifies the name of the external link.
#   description: Specifies the description of the external link.
#   url: Specifies the URL of the external link.
ADMIN_LINKS = [
    {
        'name': _('Announce'),
        'description': _('Announcement Management'),
        'url': 'https://annoucement.example.com/?q=user'
               '/login&destination=admin',
    },
]
