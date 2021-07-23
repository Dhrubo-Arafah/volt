from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, UpdateView

from .forms import MentorCreationForm, UserCreation
from .models import Mentor


def register(request):
    title = "Signup Form"
    form = UserCreation()
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('login')
        else:
            messages.success(request, 'Password Error')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'registration/register.html', context)


def become_a_mentor(request):
    form = MentorCreationForm()
    if request.method == 'POST':
        form = MentorCreationForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user_id = request.user.id
            f.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'mentor/register_form.html', context)


class MentorDetailView(DetailView):
    model = Mentor
    context_object_name = 'mentor'
    template_name = 'mentor/profile.html'


class MentorUpdateView(UpdateView):
    model = Mentor
    fields = ['image', 'occupation', 'organization', ]
    template_name = 'mentor/update_profile.html'

    def get_success_url(self, **kwargs):
        # obj = form.instance or self.object
        return reverse("mentor_detail_view", kwargs={'pk': self.object.pk})

