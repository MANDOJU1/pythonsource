from django.shortcuts import render
from .forms import UserForm


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = UserForm()

    return render(request, "register.html", {"form": form})


def common_login(request):
    pass
