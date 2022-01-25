
from django.shortcuts import render, redirect
from .forms import UserRegistraionForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
# Create your views here.

def user_register(request):

    if request.method == 'POST':
        form = UserRegistraionForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                cd['username'],
                cd['email'],
                cd['password'],
            )

            user.first_name = cd['firstname']
            user.last_name = cd['lastname']
            user.save()

            messages.success(request, 'User Register successfully', 'success')
            return redirect('home')

    else:
        form = UserRegistraionForm()

    return render(request, 'register.html', {'form':form})


def user_login(request):

	if request.method == 'POST':
		form = UserLoginForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data

			user = authenticate(request, 
            username=cd['username'], 
            password=cd['password'])

			if user is not None:
				login(request, user)
				messages.success(request, 'logged in successfully', 'success')
				return redirect('home')

			else:
				messages.error(request, 'username or password is wrong', 'danger')

	else:
		form = UserLoginForm()

	return render(request, 'login.html', {'form':form})


def user_logout(request):

    logout(request)
    messages.success(request, 'Loggout successfully', 'success')
    return redirect('home')