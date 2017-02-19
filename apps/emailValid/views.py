from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Email, Emanager
# Create your views here.
def index(request):

    context = {
        "emails": Email.objects.all()
    }

    return render(request, 'emailValid/index.html', context)
def process(request):

    if Email.objects.reg(email=request.POST['email']) == False:
        messages.add_message(request, messages.INFO, 'Hell nah, GTFO!')
    else:
        messages.add_message(request, messages.INFO, 'Good job you can type an email.')

    return redirect('/')