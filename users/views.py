import random

from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages


def dashboard_view(request):
    view = random.random()
    if view >= 0.5:
        return render(request, "users/dashboard.html")
    else:
        return render(request, "users/dashboard.html")


def election_view(request):
    view = random.random()
    if view >= 0.5:
        return render(request, 'users/election.html')
    else:
        return render(request, 'users/election.html')


def signup_view(request):

    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # user.profile.first_name = form.cleaned_data.get('first_name')
            # user.profile.last_name = form.cleaned_data.get('last_name')
            # user.profile.email = form.cleaned_data.get('email')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('success')
        else:
            messages.error(request, str(form.errors))

    view = random.random()
    if view >= 0.5:
        return render(request, 'registration/signup.html', {'form': form})
    else:
        return render(request, 'registration/signup.html', {'form': form})


def login_view(request):

    if request.method == 'GET':
        form = LoginForm()
        messages.error(request, '')
        return render(request, 'registration/login.html', {'form': form})
    else:
        # form = LoginForm(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('election')
        else:
            # form = LoginForm()
            messages.error(request, 'Username or password not correct')
            return redirect('login')         # render(request, 'registration/login.html', {'form': form})
            # return render(request, 'registration/login.html', {'form': form})


def success_view(request):
    return render(request, 'registration/success.html')
