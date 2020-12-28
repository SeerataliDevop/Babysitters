from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.shortcuts import render, redirect

from Babysitters.models import Available, AvailableMultan, AvailableIslamabad, AvailableGujranwala, AvailableKarachi, \
    AvailableSialkot, AvailablePeshawar, AvailableGujrat


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/search')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'auth/auth-login.html')


def signup_view(request):
    if request.method == "POST":
        user = User.objects.create(username=request.POST.get('username'),
                                   password=make_password(request.POST.get('password')),
                                   first_name=request.POST.get('first_name'),
                                   last_name=request.POST.get('last_name'),

                                   is_active=True,
                                   is_staff=True
                                   )
        user.save()

    return render(request, 'auth/auth-signup.html')


@login_required(login_url='login')
def search(request):
    return render(request, 'auth/search.html')


def home(request):
    return render(request, 'auth/home.html')


@login_required(login_url='login')
def log_out(request):
    logout(request)
    return redirect('home')


def contact(request):
    if request.method == "POST":
        subject = 'from babysitter website'
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        email_message = str(fname) + '\n' + str(lname) + '\n' + str(phone) + '\n' + str(email) + '\n' + str(message)
        mail = EmailMessage(subject, email_message, to=['xiratali4772@gmail.com'])
        mail.send()
        messages.success(request, 'Your message is sent')
    return render(request, 'auth/contact.html')


@login_required(login_url='login')
def log_out(request):
    logout(request)
    return redirect('home')


def about(request):
    return render(request, 'auth/about.html')


def available(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Picture = request.POST.get('Picture')
        Age = request.POST.get('Age')
        Number = request.POST.get('Number')
        Description = request.POST.get('Description')
        Availability = request.POST.get('Availability')
        Address = request.POST.get('Address')
        Skills = request.POST.get('Skills')
        Education = request.POST.get('Education')
        Email = request.POST.get('Email')
        babysitter = Available.objects.create(Name=Name, Picture=Picture, Age=Age, Number=Number,
                                              Description=Description, Availability=Availability, Address=Address,
                                              Skills=Skills, Education=Education, Email=Email)
        babysitter.save()
        return redirect('/available')

    present = Available.objects.all()
    context = {
        'present': present

    }

    return render(request, 'auth/available.html', context=context)


def available_multan(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Picture = request.POST.get('Picture')
        Age = request.POST.get('Age')
        Number = request.POST.get('Number')
        Description = request.POST.get('Description')
        Availability = request.POST.get('Availability')
        Address = request.POST.get('Address')
        Skills = request.POST.get('Skills')
        Education = request.POST.get('Education')
        Email = request.POST.get('Email')
        babysitter = AvailableMultan.objects.create(Name=Name, Picture=Picture, Age=Age, Number=Number,
                                                    Description=Description, Availability=Availability, Address=Address,
                                                    Skills=Skills, Education=Education, Email=Email)
        babysitter.save()
        return redirect('/available_multan')

    present = AvailableMultan.objects.all()
    context = {
        'present': present

    }

    return render(request, 'auth/available_multan.html', context=context)


def available_islamabad(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Picture = request.POST.get('Picture')
        Age = request.POST.get('Age')
        Number = request.POST.get('Number')
        Description = request.POST.get('Description')
        Availability = request.POST.get('Availability')
        Address = request.POST.get('Address')
        Skills = request.POST.get('Skills')
        Education = request.POST.get('Education')
        Email = request.POST.get('Email')
        babysitter = AvailableIslamabad.objects.create(Name=Name, Picture=Picture, Age=Age, Number=Number,
                                                       Description=Description, Availability=Availability,
                                                       Address=Address,
                                                       Skills=Skills, Education=Education, Email=Email)
        babysitter.save()
        return redirect('/available_islamabad')

    present = AvailableIslamabad.objects.all()
    context = {
        'present': present

    }

    return render(request, 'auth/available_islamabad.html', context=context)


def available_gujranwala(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Picture = request.POST.get('Picture')
        Age = request.POST.get('Age')
        Number = request.POST.get('Number')
        Description = request.POST.get('Description')
        Availability = request.POST.get('Availability')
        Address = request.POST.get('Address')
        Skills = request.POST.get('Skills')
        Education = request.POST.get('Education')
        Email = request.POST.get('Email')
        babysitter = AvailableGujranwala.objects.create(Name=Name, Picture=Picture, Age=Age, Number=Number,
                                                        Description=Description, Availability=Availability,
                                                        Address=Address,
                                                        Skills=Skills, Education=Education, Email=Email)
        babysitter.save()
        return redirect('/available_gujranwala')

    present = AvailableGujranwala.objects.all()
    context = {
        'present': present

    }

    return render(request, 'auth/available_gujranwala.html', context=context)


def available_karachi(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Picture = request.POST.get('Picture')
        Age = request.POST.get('Age')
        Number = request.POST.get('Number')
        Description = request.POST.get('Description')
        Availability = request.POST.get('Availability')
        Address = request.POST.get('Address')
        Skills = request.POST.get('Skills')
        Education = request.POST.get('Education')
        Email = request.POST.get('Email')
        babysitter = AvailableKarachi.objects.create(Name=Name, Picture=Picture, Age=Age, Number=Number,
                                                     Description=Description, Availability=Availability,
                                                     Address=Address,
                                                     Skills=Skills, Education=Education, Email=Email)
        babysitter.save()
        return redirect('/available_karachi')

    present = AvailableKarachi.objects.all()
    context = {
        'present': present

    }

    return render(request, 'auth/available_karachi.html', context=context)


def available_sialkot(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Picture = request.POST.get('Picture')
        Age = request.POST.get('Age')
        Number = request.POST.get('Number')
        Description = request.POST.get('Description')
        Availability = request.POST.get('Availability')
        Address = request.POST.get('Address')
        Skills = request.POST.get('Skills')
        Education = request.POST.get('Education')
        Email = request.POST.get('Email')
        babysitter = AvailableSialkot.objects.create(Name=Name, Picture=Picture, Age=Age, Number=Number,
                                                     Description=Description, Availability=Availability,
                                                     Address=Address,
                                                     Skills=Skills, Education=Education, Email=Email)
        babysitter.save()
        return redirect('/available_sialkot')

    present = AvailableSialkot.objects.all()
    context = {
        'present': present

    }

    return render(request, 'auth/available_sialkot.html', context=context)


def available_peshawar(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Picture = request.POST.get('Picture')
        Age = request.POST.get('Age')
        Number = request.POST.get('Number')
        Description = request.POST.get('Description')
        Availability = request.POST.get('Availability')
        Address = request.POST.get('Address')
        Skills = request.POST.get('Skills')
        Education = request.POST.get('Education')
        Email = request.POST.get('Email')
        babysitter = AvailablePeshawar.objects.create(Name=Name, Picture=Picture, Age=Age, Number=Number,
                                                      Description=Description, Availability=Availability,
                                                      Address=Address,
                                                      Skills=Skills, Education=Education, Email=Email)
        babysitter.save()
        return redirect('/available_peshawar')

    present = AvailablePeshawar.objects.all()
    context = {
        'present': present

    }

    return render(request, 'auth/available_peshawar.html', context=context)


def available_gujrat(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Picture = request.POST.get('Picture')
        Age = request.POST.get('Age')
        Number = request.POST.get('Number')
        Description = request.POST.get('Description')
        Availability = request.POST.get('Availability')
        Address = request.POST.get('Address')
        Skills = request.POST.get('Skills')
        Education = request.POST.get('Education')
        Email = request.POST.get('Email')
        babysitter = AvailableGujrat.objects.create(Name=Name, Picture=Picture, Age=Age, Number=Number,
                                                    Description=Description, Availability=Availability, Address=Address,
                                                    Skills=Skills, Education=Education, Email=Email)
        babysitter.save()
        return redirect('/available_gujrat')

    present = AvailableGujrat.objects.all()
    context = {
        'present': present

    }

    return render(request, 'auth/available_gujrat.html', context=context)


def packages(request):
    return render(request, 'auth/packages.html')
