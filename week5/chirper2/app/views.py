from django.shortcuts import render
from app.models import Chirp

def index_view(request):
    print(request.POST)
    if request.POST:
        chirp_body = request.POST["chirp_body"]
        if chirp_body != "":
            Chirp.objects.create(body=chirp_body)
    context = {
    "chirps" : Chirp.objects.all().order_by("-created")
    }
    return render(request, "index.html", context)

def about_view(request):
    print("Hello" + "=" * 20)
    print(request.GET)
    print(request.POST)
    message = request.POST.get("message", "")
    voice = request.POST.get("voice", "")
    print(message,voice)
    return render(request, "about.html")
