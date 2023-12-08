from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Group, Subject

# Create your views here.
def home_view(request):
    groups = Group.objects.all()
    context = {"groups": groups}
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

@login_required(login_url="login")
def groups_view(request):
    groups = Group.objects.all()
    context = {"groups": groups}
    return render(request, "group/groups.html", context)

@login_required(login_url="login")
def group_view(request, group_id):
    group = Group.objects.get(id=group_id)
    group_single_view = True
    subjects = Subject.objects.filter(associated_group=group)
    context = {"group": group, "group_single_view": group_single_view, "subjects": subjects}
    return render(request, "group/group.html", context)

@login_required(login_url="login")
def add_group_view(request):
    form_action = "Add"
    error = ""

    if request.method == "POST":
        name = request.POST.get("name")
        currently_active = request.POST.get("currently_active")

        if name is not None:

            if currently_active == "Yes":
                currently_active = True
            else:
                currently_active = False

            group = Group.objects.create(
                name=name,
                currently_active=currently_active,
                associated_with=request.user,
            )
            previous_page = request.GET.get('next', '/')
            return redirect(previous_page)

        else:
            error = "Please Donot Leave Name Empty!"

    context = {"form_action": form_action, "error": error}
    return render(request, "group/group_form.html", context)

@login_required(login_url="login")
def update_group_view(request, group_id):
    form_action = "Update"
    error = ""

    group = Group.objects.get(id=group_id)

    name = group.name
    currently_active = group.currently_active

    if request.method == "POST":

        if name is not None:

            name = request.POST.get("name")
            currently_active = request.POST.get("currently_active")

            if currently_active == "Yes":
                currently_active = True
            else:
                currently_active = False

            group.name = name
            group.currently_active = currently_active
            group.save()

            previous_page = request.GET.get('next', '/')
            return redirect(previous_page)

        else: 
            error = "Please Donot Leave Name Empty!"

    context = {"form_action": form_action, "error": error, "name": name, "currently_active": currently_active}
    return render(request, "group/group_form.html", context)

@login_required(login_url="login")
def delete_group_view(request, group_id):
    group = Group.objects.get(id=group_id)

    currently_active = group.currently_active

    if currently_active:
        item_category = "Currently Active Group"
    else:
        item_category = "Group"

    item = group.name.title()

    if request.method == "POST":
        group.delete()

        previous_page = request.GET.get('next', '/')
        return redirect(previous_page)

    context = {"item_category": item_category, "item": item}
    return render(request, "delete.html", context)

@login_required(login_url="login")
def subjects_view(request, group_id):
    group = Group.objects.get(id=group_id)
    subjects = Subject.objects.filter(associated_group=group)
    context = {"subjects": subjects}
    return render(request, "subject/subjects.html", context)

@login_required(login_url="login")
def subject_view(request, group_id, subject_id):
    subject = Subject.objects.get(id=subject_id)
    subject_single_view = True
    context = {"subject": subject, "subject_single_view": subject_single_view}
    return render(request, "subject/subject.html", context)    

@login_required(login_url="login")
def add_subject_view(request, group_id):
    form_action = "Add"
    error = ""

    associated_group = Group.objects.get(id=group_id)

    if request.method == "POST":
        name = request.POST.get("name")

        if name is not None:

            subject = Subject.objects.create(
                name=name,
                associated_group=associated_group
            )
            previous_page = request.GET.get('next', '/')
            return redirect(previous_page)

        else:
            error = "Please Donot Leave Name Empty!"

    context = {"form_action": form_action, "error": error, "associated_group": associated_group}
    return render(request, "subject/subject_form.html", context)

@login_required(login_url="login")
def update_subject_view(request, group_id, subject_id):
    form_action = "Update"
    error = ""

    associated_group = Group.objects.get(id=group_id)
    subject = Subject.objects.get(id=subject_id)

    name = subject.name

    if request.method == "POST":

        if name is not None:

            name = request.POST.get("name")

            subject.name = name
            subject.save()

            previous_page = request.GET.get('next', '/')
            return redirect(previous_page)

        else: 
            error = "Please Donot Leave Name Empty!"

    context = {"form_action": form_action, "error": error, "name": name, "associated_group": associated_group}
    return render(request, "subject/subject_form.html", context)

@login_required(login_url="login")
def delete_subject_view(request, group_id, subject_id):
    
    group = Group.objects.get(id=group_id)
    subject = Subject.objects.get(id=subject_id)

    item_category = f"Topic Of Group {group.name.title()}"

    item = subject.name.title()

    if request.method == "POST":
        subject.delete()

        previous_page = request.GET.get('next', '/')
        return redirect(previous_page)

    context = {"item_category": item_category, "item": item}
    return render(request, "delete.html", context)
