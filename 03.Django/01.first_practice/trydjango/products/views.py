from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kargs):
    return render(request, "index.html", {})