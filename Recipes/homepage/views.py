from django.shortcuts import render


def get_homepage(request):
    template_name = 'homepage/homepage.html'
    return render(request, template_name)

