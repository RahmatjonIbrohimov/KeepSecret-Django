from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserModel
from .forms import SignUpForm, UserProfileForm, UserUpdateForm


# Create your views here.
def SignUpView(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('user_info')

    else:
        user_form = SignUpForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


class LoginViews(LoginView):
    template_name = 'login.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = UserModel
    form_class = UserUpdateForm
    template_name = 'update.html'
    success_url = 'user_info'

    def get_object(self, queryset=None):
        return self.request.user.usermodel


@login_required
def ProfileViews(request):
    user = request.user
    return render(request, 'info.html', {'user': user})


def LogoutViews(request):
    logout(request)
    return redirect('/')


