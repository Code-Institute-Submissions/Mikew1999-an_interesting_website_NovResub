''' Render '''
from django.shortcuts import render, redirect
from products.models import Category
from .models import ContactMe, Newsletter
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

    if request.POST:
        if 'newsletter_email' in request.POST:
            email_input = str(request.POST['newsletter_email'])
            email_address = Newsletter.objects.filter(email=email_input)[:1].values('email')
            if email_address:
                if email_input == email_address[0]['email']:
                    messages.add_message(request, messages.ERROR,
                        'You have already signed up for our newsletter')
            else:
                try:
                    new_email = Newsletter(email=email_input)
                    new_email.save()
                    messages.add_message(request, messages.SUCCESS,
                        'You have successfully signed up for our newsletter')
                except:
                    messages.add_message(request, messages.ERROR,
                        'Something went wrong, please try again and if the issue continues please contact support@aninterestingwebsite.com')
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

                messages.add_message(request, messages.SUCCESS, 'Email sent, We will be in touch shortly!')
                return redirect('home')
            except:
                print("email not sent")
                messages.add_message(request, messages.ERROR, 'Sending email not successful, please check your email address and password.')
                return redirect('contact_us')

    context = {
        'form': form,
    }

    return render(request, 'home/contact_us.html', context)


def about_us(request):
    ''' Returns the about us page '''
    return render(request, 'home/about_us.html')


def privacy_policy(request):
    ''' Returns Privacy Policy Page '''
    return render(request, 'home/privacy_policy.html')
