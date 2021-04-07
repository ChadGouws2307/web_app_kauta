from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import SignUpForm, LoginForm, UserPermissionForm
from .models import UserPermission

import user_analytics.analytics as ana


def signup_view(request):
    template = ana.choose_template_option('registration/signup.html', 'home_v2.html')
    if request.method == 'GET':
        form = SignUpForm()
        perm = UserPermissionForm()
        return render(request, template, {'form': form, 'perm': perm})
    else:
        form = SignUpForm(request.POST)
        perm = UserPermissionForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            if perm.is_valid():
                permission = perm.save(commit=False)
                _create_user_permissions(request.user, permission.permission)
            return redirect('success')
        else:
            messages.error(request, str(form.errors))
        return render(request, template, {'form': form, 'perm': perm})


def _create_user_permissions(user, permission):
    instance = UserPermission(user=user, permission=permission, newsletter=permission, email_marketing=permission,
                              product_launch_and_updates=permission, investing_ideas=permission)
    instance.save()


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
            return redirect('about')
        else:
            # form = LoginForm()
            messages.error(request, 'Username or password not correct')
            return redirect('login')         # render(request, 'registration/login.html', {'form': form})
            # return render(request, 'registration/login.html', {'form': form})


def success_view(request):
    return render(request, 'registration/success.html')
