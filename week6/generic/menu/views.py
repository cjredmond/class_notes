from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from menu.models import Special,Profile
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


class IndexView(ListView):
    template_name = "index.html"
    model = Special

class ProfileUpdateView(UpdateView):
    template_name = "profile.html"
    success_url = reverse_lazy('profile_view')
    fields= ('access_level',)
    def get_object(self):
        return Profile.objects.get(user=self.request.user)
    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)




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
