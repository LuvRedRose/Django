from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "Title" : 'Home',
    }

    return render(request, 'home/index.html', context)