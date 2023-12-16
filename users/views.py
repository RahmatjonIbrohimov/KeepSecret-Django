from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import UserModel
from .forms import SignUpForm


# Create your views here.
def SignUpViews(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            UserModel.objects.create(
                user=user,
                full_name=form.cleaned_data.get('full_name'),
                phone_number=form.cleaned_data.get('phone_number')
            )

            return HttpResponse('Done!')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})
