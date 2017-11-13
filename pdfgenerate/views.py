# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render
from .utils import generatePdf,sendMail

# Create your views here.


def index(request):
    if request.method == 'POST':
        # try:
        #     attechment = "invoice.html"
            attechment = ""
            file=request.FILES['file']

            sendMail(name="nitesh",email="nkscoder@gmail.com",template="UserSuccessTemplate.html",subject="send Mail",attechment = attechment,upload = file)

        # except Exception as e:
        #
        #     return render(request, "index.html", {"msg": e})
    return render(request,"index.html")