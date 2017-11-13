from django.conf import settings
from django.contrib.auth.models import User
from .models import *
# from django.contrib.auth.models import User

from pprint import pprint

from django.contrib.auth import authenticate


from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from django.conf import settings



def generatePdf(*args,**kwargs):
   import pdfkit
   str_data = kwargs.pop("html")
   return pdfkit.from_string(str_data,False)



def sendMail(*args,**kwargs):
   """
   function to send the mail
   """
   adminemail=kwargs.pop('email')
   name=kwargs.pop('name')
   attechment=kwargs.pop('attechment')
   fileupload=kwargs.pop('upload')
   subject=kwargs.pop("subject")
   plaintext = get_template('email.txt')
   htmly = get_template(kwargs.pop('template'))
   user_context = {'name':name, 'email':adminemail}
   text_content = plaintext.render(user_context)
   email = EmailMultiAlternatives(subject, text_content,to=[adminemail])

   if attechment:
       html_content = htmly.render(user_context)
       html = get_template(attechment).render(user_context)
       file_to_be_sent = generatePdf(html=html)
       email.attach("Report.pdf", file_to_be_sent, "application/pdf")
       email.attach_alternative(html_content, "text/html")

   if fileupload:
       # fileupload=kwargs.pop('upload')
       email.attach(fileupload.name, fileupload.read(), fileupload.content_type)
       email.attach_alternative(htmly, "text/html")

   email.send()

   return
