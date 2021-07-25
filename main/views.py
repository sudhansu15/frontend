from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.


def index(request):
    """ stockdata = Index.objects.order_by('-date')[0:1] """
    # operation = Index.objects.raw("SELECT nepse FROM "Rest_API_index" ORDER BY "date" DESC LIMIT 1")
    # a = Index.objects.raw("SELECT nepse FROM Rest_API_index ORDER BY date DESC LIMIT 1")
    return render(request, 'index.html')


""" def aboutus(request):
    team = TeamMember.objects.all()
    return render(request, 'aboutus.html', {'team': team}) """


def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
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
                        username=username, password=password1, email=email)
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


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout(request):
    # Delete the user session
    request.session.flush()
    auth.logout(request)
    return redirect('/')


""" def search(request):
    qstock = request.GET.get('query')
    # Stock_q = DataStock.objects.filter(Symbol=qstock).order_by('-Date')[0:1].get()
    Stock_q = DataStock.objects.filter(Symbol=qstock).order_by('-Date')[0:1]
    # Stock_q = DataStock.objects.filter(Symbol=qstock).order_by('Date').last()
    # Stock_q = DataStock.objects.order_by('Symbol')[0:1]
    print(Stock_q.query)
    print(Stock_q)
    print(qstock)

    Stock = {
        'Symbol': qstock,
    }
    return render(request, 'search.html', {'stocks': Stock_q, 'stock_symbol': qstock})


def chart(request, stock_symbol):
    return render(request, 'charter.html') """
