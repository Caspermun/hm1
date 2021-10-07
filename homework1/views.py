from django.shortcuts import render


def index(request):
    name = 'Mirlanov Nursulan'
    return render(request, 'index.html', locals())

def index2(request):
    name = 'Luchi Baker'
    return render(request, 'index2.html', locals())

def index3(request):
    name = 'Jayne Francis'
    return render(request, 'index3.html', locals())

def index4(request):
    name = 'Zarah Callahan'
    return render(request, 'index4.html', locals())

def index5(request):
    name = 'Renae Jones'
    return render(request, 'index5.html', locals())