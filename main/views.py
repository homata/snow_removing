from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import ugettext as _

from django.shortcuts import get_object_or_404

import os

import snow.settings as settings
import tools.logs as logs
from tools.utils import utils
import traceback

#----------------------------
def index(request):
    """
    index()
    """

    #logs.debug("index()")

    try:
        contexts = {}

        # 現在ログインしている?
        #if request.user.is_authenticated:
        #    contexts['user'] = {"username": request.user.username, "user_id": request.user.id, "is_authenticated": True}

        items = []
        for ii in range(10):
            item = {}
            item['name']  = "%d: xxxxxx" % (ii+1)
            item['sub_name']  = _("zzzzzz")
            items.append(item)

        contexts['items'] = items

        return render(request, 'main/index.html', contexts)

    except Exception as e:
        traceback.print_exc()
        return render(request, 'main/index.html', {})

    except:
        logs.error('system error: other error')
        return render(request, 'main/index.html', {})
