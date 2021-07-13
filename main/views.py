from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect, HttpResponse


""" from django.shortcuts import render, redirect, HttpResponse
from .models import tabledata
from django.contrib.auth.models import User, auth """
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'post':
        username = request.post['username']
        email = request.post['eamil']
        password1 = request.post['password1']
        password2 = request.post['password2']

        user = user.objects.create_user(
            username=username, password=password1, email=email)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request, 'signup.html')


""" *********************************************************************************************  """


""" def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    print('Username taken')
                    messages.info(request, 'Username Taken')
                    # return HttpResponseRedirect('')
                    return redirect('index')
                elif User.objects.filter(email=email).exists():
                    print('Email taken')
                    messages.info(request, 'Email Taken')
                    # return HttpResponseRedirect('')
                    return redirect('index')
                else:
                    user = User.objects.create_user(
                        username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                    print('user created')
                    user.save()
            # return HttpResponse('User Created.')
            else:
                print('password not matching')
                messages.info(request, 'Password Not Matching')
                # return HttpResponseRedirect('')
                return redirect('index')
            # redirect to a new URL:
            return HttpResponseRedirect('/')
            # return redirect('/')
            # return render(request, 'result.html', {'first_name' : first_name})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()
        return render(request, 'index.html', {'form': form})
 

 def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            print('Successfully userform data taken.')
            print(request.POST)

            if password1 == password2:
                if User.objects.filter(username=username):
                    print('Username Taken')
                    messages.info(request, 'Username Taken')
                    return redirect('signup')
                elif User.objects.filter(email=email):
                    print('Email Taken')
                    messages.info(request, 'Email Taken')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(
                        username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                    print('user created')
                    user.save()
                    return redirect('index')
        else:
            print('password not matching')
            messages.info(request, 'Password Not Matching')
            return redirect('signup')

    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

 
 def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                print("logged In User")
                auth.login(request, user)

                return redirect('index')
            else:
                messages.info(request, "Invalid Username or Password")
                print('Not Logged In')
                return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
 
"""


def logout(request):
    auth.logout(request)
    return redirect('/')


def search(request):
    return render(request, "")
