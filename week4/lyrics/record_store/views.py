from django.shortcuts import render
from django.http import HttpResponse
import datetime
from record_store.models import Song
# Create your views here.
def index_view(request):
    context = {
        "my_name": "CONNOR",
        "now": datetime.datetime.now(),
        "all_songs": Song.objects.all()
    }

    return render(request, "index.html", context)
    #return HttpResponse()
