from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from Authentication_App.forms import RegistrationForm, ProfilePicForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages



# Create your views here.


def user_signup(request):
    form =RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Authentication_App:login'))
    dictionary = {
        'form': form,
    }
    return render(request, 'Authentication_App/signup.html', context=dictionary)


def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    dictionary = {
        'form': form,
    }

    return render(request, 'Authentication_App/login.html', context=dictionary)


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Authentication_App:login'))


@login_required
def user_profile(request):
    user = request.user

    dictionary ={
        'user': user,
    }

    return render(request, 'Authentication_App/user_profile.html', context=dictionary)


@login_required
def update_dp(request):
    user = request.user
    instance = getattr(user, 'user_profile', None)
    form = ProfilePicForm(request.POST or None, request.FILES or None, instance=instance)
    if request.method == 'POST' and form.is_valid():
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        return HttpResponseRedirect(reverse('Authentication_App:user_profile'))
    context = {
        'form': form,
    }
    return render(request, 'Authentication_App/update_dp.html', context=context)

@login_required
def update_profile(request):
    form = UpdateProfileForm(instance = request.user)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Authentication_App:user_profile'))
    dictionary ={
        'form': form,
    }
    return render(request,'Authentication_App/update_profile.html',context=dictionary)


@login_required
def delete_dp(request):
    dp = request.user.user_profile.profile_pic.delete()
    return HttpResponseRedirect(reverse('Authentication_App:user_profile'))



@login_required
def change_password(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user= request.user, data = request.POST)
        if form.is_valid():
            obj = form.save()
            update_session_auth_hash(request, obj)
            messages.success(request,'Password changed successfully')
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request,'Error Password! Change The following.')
    dictionary = {
        'form': form,
    }
    return render(request, 'Authentication_App/change_password.html', context=dictionary)


@login_required
def delete_account(request):
    user= request.user.delete()
    return HttpResponseRedirect(reverse('Authentication_App:login'))