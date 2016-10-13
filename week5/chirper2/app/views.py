from django.shortcuts import render
from app.models import Chirp
from app.forms import ChirpForm
from django.views import View

def index_view(request):
    if request.POST:
        instance = ChirpForm(request.POST)
        if instance.is_valid():
            instance.save()

    context = {
    "chirps" : Chirp.objects.all().order_by("-created"),
    "form" : ChirpForm()
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

class ChirpView(View):
    def get(self, request):
        return render(request, "chirps.html")

    def post(self, request):
        return render(request, "chirps.html")
