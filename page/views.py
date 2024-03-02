from django.shortcuts import render


# Create your views here.
def index(request):
    context = {

    }
    return render(request, "index.html", context)


def handler404(request, exception):
    return render(request, 'index.html')
