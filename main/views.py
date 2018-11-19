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

        contexts['items'] = [
            { "rank":  1, 'name': "avocado",    "locate": "名寄市朝日"},
            { "rank":  2, 'name': "strawberry", "locate": "名寄市弥生"},
            { "rank":  3, 'name': "plum",       "locate": "名寄市瑞穂"},
            { "rank":  4, 'name': "persimmon",  "locate": "名寄市砺波"},
            { "rank":  5, 'name': "cherry",     "locate": "名寄市風連町東風連"},
            { "rank":  6, 'name': "watermelon", "locate": "名寄市内淵"},
            { "rank":  7, 'name': "banana",     "locate": "名寄市東六条北"},
            { "rank":  8, 'name': "papaya",     "locate": "名寄市東二条北"},
            { "rank":  9, 'name': "mango",      "locate": "名寄市日彰"},
            { "rank": 10, 'name': "peach",      "locate": "名寄市西八条南"}
        ]

        return render(request, 'main/index.html', contexts)

    except Exception as e:
        traceback.print_exc()
        return render(request, 'main/index.html', {})

    except:
        logs.error('system error: other error')
        return render(request, 'main/index.html', {})
