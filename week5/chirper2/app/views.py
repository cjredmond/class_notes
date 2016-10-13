from django.shortcuts import render
from app.models import Chirp
from app.forms import ChirpForm
from django.views import View
from django.views.generic import TemplateView
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

class ChirpView(TemplateView):
    template_name = "chirps.html"

    def get_context_data(self):
        context = {
        "all_chirps" : Chirp.objects.all(),

        }
        return context
