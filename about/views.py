from django.shortcuts import render, redirect
import random


def home_view(request):
    view = random.random()
    if view >= 0.5:
        return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})


def about_view(request):
    view = random.random()
    if view >= 0.5:
        return render(request, 'about.html', {})
    else:
        return redirect('about_v2')


def about_view_v2(request):
    return render(request, 'about_v2.html', {})


def pricing_view(request):
    view = random.random()
    if view >= 0.5:
        return render(request, 'pricing_index.html', {})
    else:
        return redirect('pricing_index_v2')


def pricing_view_v2(request):
    return render(request, 'pricing_index_v2.html', {})


def terms_view(request):
    return render(request, 'terms_and_conditions.html', {})


def privacy_view(request):
    return render(request, 'privacy_notice.html', {})

