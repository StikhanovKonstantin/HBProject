from django.shortcuts import render


def get_about(request):
    return render(request, 'about/about.html')
