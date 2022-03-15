from django.shortcuts import render

# Create your views here.
def bikehome_view(request, *args, **kargs):
    return render(request, "bikehome.html", {})