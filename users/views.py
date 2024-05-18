from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# from django.http import HttpResponse


# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("posts:list")

    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # process continue nav ...
            # combine with the @login_request tag. set the next URL
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")

    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("homepage")
