#from django.http import HttpResponseServerError
#from django.http import Http404
#from django.http import HttpResponseBadRequest
from django.http import (
    HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound,
    HttpResponseServerError,
)
from django.template import Context, Engine, TemplateDoesNotExist, loader

ERROR_TEMPLATE_NAME = 'error.html'

"""
https://docs.djangoproject.com/ja/2.0/_modules/django/views/defaults/
"""

#----------------------------
def error(message="", template_name=ERROR_TEMPLATE_NAME):
    """
    error
    """

    context = {
        'message': message,
    }

    try:
        template = loader.get_template(template_name)
        body = template.render(context)
        content_type = None             # Django will use DEFAULT_CONTENT_TYPE

    except TemplateDoesNotExist:
        template = Engine().from_string(
            '<h1>An error occurred.</h1>'
            '<p>{{ message }}</p>'
            '<p><a href="javascript:history.back()">&lt; Back</a></p>'
            )

        body = template.render(Context(context))
        content_type = 'text/html'

    return HttpResponseBadRequest(body, content_type=content_type)