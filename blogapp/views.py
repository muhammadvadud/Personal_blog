from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from .models import Education,Experience,Setting,Portfolio,Blog,Contact,About
from telebot import TeleBot

bot = TeleBot("5996278075:AAGcKiC6T3wD-jA-rbFd-odjqr8MGlF6ui8")

class HomePage(View):



    def get(self,request):

        context = {}
        context['Experience'] = Experience.objects.all()
        context['Education'] = Education.objects.all()
        context['Setting'] = Setting.objects.all()
        context['Portfolio'] = Portfolio.objects.all()
        context['Blog'] = Blog.objects.all()
        context['Contact'] = Contact.objects.all()
        context['u'] = About.objects.all().first()




        return render(request,"index.html",context)


    def post(self,request):
        data = request.POST
        name = data["name"]
        email = data["email"]
        message = data["message"]

        Contact.objects.create(name=name,email=email,message=message)
        bot.send_message(5543472877, f"Yangi xabar keldi \n\nism:{name}\n\nemail:{email}\n\n{message}")
        return redirect(reverse("home"))
