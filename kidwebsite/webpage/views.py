from django.shortcuts import render


def index(request):
    return render(request, 'webpage/home.html')


def gallery(request):
    return render(request, 'webpage/gallery.html')


def about(request):
    return render(request, 'webpage/about.html')