from django.shortcuts import render
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
        return render(request, 'about_1.html', {})


def pricing_view(request):
    view = random.random()
    if view >= 0.5:
        return render(request, 'pricing_index.html', {})
    else:
        return render(request, 'pricing_index_v2.html', {})

