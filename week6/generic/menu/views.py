from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from menu.models import Special
from django.views.generic.edit import UpdateView, DeleteView

class IndexView(ListView):
    template_name = "index.html"
    model = Special

class ProfileView(TemplateView):
    template_name = "profile.html"

class SpecialUpdateView(UpdateView):
    model = Special
    success_url = "/"
    fields = ('title', 'description', 'cost')

    def get_queryset(self):
        if self.request.user.profile.access_level == 'o':
            return Special.objects.all()
        return Special.objects.filter(created_by=self.request.user)

class SpecialDeleteView(DeleteView):
    model = Special
    success_url = "/"

    def get_queryset(self):
        if self.request.user.profile.access_level == 'o':
            return Special.objects.all()
        return []
