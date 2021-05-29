from django.http import request
from django.shortcuts import render
import pyttsx3

# Create your views here.
def index(request):
    def indexspok():
        kothatuku="Hi, Wellcome on, Afnan Islam Akash, Website"
        kotha=pyttsx3.init()
        kotha.say(kothatuku)
        kotha.runAndWait()
    return render(request,"index.html",indexspok())
def about(request):
    def aboutspok():
        kothatuku="About,Afnan Islam Akash"
        kotha=pyttsx3.init()
        kotha.say(kothatuku)
        kotha.runAndWait()
    return render(request,"about.html",aboutspok())
def skill(request):
    def aboutspok():
        kothatuku="About,Afnan Islam Akash,Skills"
        kotha=pyttsx3.init()
        kotha.say(kothatuku)
        kotha.runAndWait()
    return render(request,"skill.html",aboutspok())
def contact(request):
    def contactspok():
        kothatuku="we are, happy to know, You want contact, Afnan Islam Akash"
        kotha=pyttsx3.init()
        kotha.say(kothatuku)
        kotha.runAndWait()
    return render(request,"contact.html",contactspok())
def error(request,exception):
    return render(request,'404.html')
def error500(request):
    def contactspok():
        kothatuku="we are, happy to know, You want contact, Afnan Islam Akash"
        kotha=pyttsx3.init()
        kotha.say(kothatuku)
        kotha.runAndWait()
    return render(request,'404.html',contactspok())