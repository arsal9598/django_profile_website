from django.shortcuts import render, redirect
from datetime import date
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def index(request):
    def calculate_age(dtob):
        today = date.today()
        return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))
    age = calculate_age(date(2000,10,17))
    template = "index.html"
    context = {'age': age}
    return render(request, template, context=context)
