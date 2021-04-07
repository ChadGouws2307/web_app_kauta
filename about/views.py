from django.shortcuts import render

from users.forms import EmailForm

from user_analytics import analytics as ana


def home_view(request):
    template = ana.choose_template_option('home.html', 'home_v2.html')
    if request.method == 'GET':
        form = EmailForm()
        ind = ''
    else:
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save()
            email.save()
            ind = 'Thank you!'
        else:
            ind = ''

        return render(request, template, {'form': form, 'ind': ind})
    context = {
        'form': form,
        'ind': ind,
    }
    return render(request, template, context)


def about_view(request):
    template = ana.choose_template_option('about.html', 'about_v2.html')
    return render(request, template, {})


def pricing_view(request):
    template = ana.choose_template_option('pricing_index.html', 'pricing_index_v2.html')
    return render(request, template, {})


def terms_view(request):
    return render(request, 'terms_and_conditions.html', {})


def privacy_view(request):
    return render(request, 'privacy_notice.html', {})
