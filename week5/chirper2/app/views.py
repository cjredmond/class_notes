from django.shortcuts import render
from app.models import Chirp, Vote
from app.forms import ChirpForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def about_view(request):
    print("Hello" + "=" * 20)
    print(request.GET)
    print(request.POST)
    message = request.POST.get("message", "")
    voice = request.POST.get("voice", "")
    print(message,voice)
    return render(request, "about.html")

class ChirpView(ListView):
    template_name = "chirps.html"
    model = Chirp

class ChirpDetailView(DetailView):
    model = Chirp

class ChirpCreateView(CreateView):
    model = Chirp
    success_url = "/"
    fields = ('body',)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

class ChirpUpdateView(UpdateView):
    model = Chirp
    success_url = "/"
    fields = ('body',)



class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/" #show reverse_lazy

class ChirpVoteView(CreateView):
    model = Vote
    fields = ('value',)
    success_url = "/"

    def form_valid(self, form):
        try:
            Vote.objects.get(user=self.request.user, chirp_id=self.kwargs['pk']).delete()
        except Vote.DoesNotExist:
            pass
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.chirp = Chirp.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
