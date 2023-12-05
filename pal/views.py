from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

# Create your views here.
def home_view(request):
    context = {}
    return render(request, "home.html", context)

def register_view(request):
    form_action = "Register"
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == None and password == None:
            error = "You Can Leave Neither Username Or Password Empty!"
        elif len(password) < 8:
            error = "Your Password Must Atleast Be 8 Characters Long!"
        else:
            try:
                user = User.objects.get(username = username)
                error = "User With Username Alrady Exists!"
            except User.DoesNotExist:
                user = User.objects.create(
                    username=username,
                    password=password
                )
                login(request, user)
                return redirect("home")

    context = {"form_action": form_action, "error": error}
    return render(request, "auth_form.html", context)

def login_view(request):
    form_action = "Login"
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == None and password == None:
            error = "You Can Leave Neither Username Or Password Empty!"
        else:
            try:
                user = User.objects.get(username=username, password=password)
                login(request, user)
                return redirect("home")
            except User.DoesNotExist:
                error = "An Error Occured During Login! Maybe Invalid Credentials!"            

            try:
                user = User.objects.get(username = username)
            except User.DoesNotExist:
                error = "User With Username Does Not Exist!"

    context = {"form_action": form_action, "error": error}
    return render(request, "auth_form.html", context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")