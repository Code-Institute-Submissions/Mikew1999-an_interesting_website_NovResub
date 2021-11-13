''' Render '''
from django.shortcuts import render, redirect
from products.models import Category
from .models import ContactMe
from .forms import ContactMeForm
from django.contrib import messages
from an_interesting_site import settings
import smtplib
import ssl


def index(request):
    ''' Shows home page '''
    username = None
    user = request.user
    categories = Category.objects.all()

    if user.is_authenticated:
        username = request.user.username

    context = {
        'username': username,
        'categories': categories,
    }

    return render(request, 'home/index.html', context)


def contact(request):
    ''' Returns contact form and handles form input '''
    form = ContactMeForm()

    if request.POST:
        form = ContactMeForm(request.POST)
        if form.is_valid():
            # Field forms
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Saves message
            new_message = ContactMe(name=name, email=email, message=message)
            new_message.save()
            # Sends email
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = form.cleaned_data['email']
            password = request.POST['password']
            receiver_email = "mikewaltdev@gmail.com"
            try:
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
                return redirect('home')
            except:
                print("email not sent")
                messages.add_message(request, messages.ERROR, 'Sending email not successful, please check your email address and password.')
                return redirect('contact_us')

    context = {
        'form': form,
    }

    return render(request, 'home/contact_us.html', context)
