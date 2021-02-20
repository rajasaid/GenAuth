from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
    return render(request, "Authen/index.html")

def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    myUser = authenticate(request, username=username, password=password)
    if myUser is not None:
        auth_login(request, myUser)
        context = {

        }
        return HttpResponse("<h1>Signed In Successfully</h1>") #render(request, "orders/menu.html", context)
    else:
        return HttpResponse("<h1>Error, Can't Login</h1>")

@csrf_protect
def logout(request):
    auth_logout(request)
    redirect(request, 'index')

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

def register(request):
    username = request.POST.get("uname")
    password = request.POST.get("pass")
    email = request.POST.get("email")
    groupname = request.POST.get("groupname")
    repass = request.POST.get("repass")
    if (password != repass):
        return render(request,"Authen/register_invalid_confirm")

    if not validateEmail(email):
        return render(request,"Authen/register_invalid_email.html")

    userObj = User.objects.filter(username=username)
    if userObj.exists():
        return render(request,"Authen/register_invalid_username.html")
    emailObj = User.objects.filter(email=email)
    if emailObj.exists():
        return render(request,"Authen/register_email_exists.html")
    group = groupname.lower()
    new_group, created = Group.objects.get_or_create(name=group)
    newUser = User.objects.create_user(username, email, password, is_staff=False)
    if newUser is not None:
        newUser.groups.add(new_group)
        newUser.save()
        # render main menu page
        context = {
        }
        return HttpResponse("<h1>Registerion successful...</h1>") #render(request, "orders/menu.html", context)
    else:
        return HttpResponse("error creating newUser")
