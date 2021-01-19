from django.shortcuts import render
from . import models


# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        ins = models.ContactForm(name=name, email=email, message=message)
        ins.save()

    return render(request, "index.html")




