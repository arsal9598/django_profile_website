from django.shortcuts import render, redirect
from datetime import date
from .forms import ContactForm
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

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    ['arsal9598@gmail.com'],
                    fail_silently=False,
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    template = "success.html"
    context = {}
    return render(request, "success.html", context=context)
