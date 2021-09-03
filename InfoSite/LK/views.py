from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .forms import LoginForm, UserRegistrationForm, ProfileForm, LkpageForm
from .forms import LoginForm
from .models import Profile, Lkpage


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'LK/profile.html')
            else:
                return render(request, 'LK/login.html')
        else:
            return render(request, 'LK/profile.html')
    else:
        form = LoginForm()
    return render(request, 'LK/login.html', {'form': form,
                                             'news': Lkpage.objects.filter(user=request.user).order_by('-data_page')})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return render(request, 'LK/registr_done.html',)
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    return render(request, 'LK/CheckIn.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def edit(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile,
                                       files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return render(request, 'LK/profile.html', {'profile_form': profile_form,
                                                       'news': Lkpage.objects.filter(user=request.user).order_by('-data_page')})
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request,'LK/user_update.html',{'profile_form': profile_form})

@login_required
def PersonalPage(request):
    user = request.user
    return render(request, 'LK/profile.html', {'user': user,
                  'news': Lkpage.objects.filter(user=request.user).order_by('-data_page')})

def AddNews(request):
    if request.method == 'POST':
        user = request.user
        form_add = LkpageForm(request.POST, request.FILES)
        if form_add.is_valid():
            news = form_add.save(commit=False)
            news.user = request.user
            news.save()
            return render(request, 'LK/profile.html', {'news': Lkpage.objects.filter(user=request.user).order_by('-data_page')})
    else:
        form_add = LkpageForm()
    return render(request, 'LK/AddNewPage.html', {'form_add': form_add})
