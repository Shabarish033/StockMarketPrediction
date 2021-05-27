from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm, Number_of_Companies_Form

def Home(request):
    if request.method == 'POST':
        username = request.POST.get('username') #get the username and password
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password) #authenticating the user
         #check if user already exists
        if user is not None:
            login(request, user)
            return redirect('Number_of_Companies') #The first page after logging in
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'FirstPage/Home.html', context)

def logoutUser(request):
    logout(request)
    return redirect('Home')


def Register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for ' + user)
            return redirect('Home') #once registration is complete user goes to Login Page
    context = {'form':form}
    return render(request, 'FirstPage/Register.html', context)

def ForgotPassword(request):
    context = {}
    return render(request, 'FirstPage/ForgotPassword.html')

@login_required(login_url = 'Home')
def Number_of_Companies(request):
    form = Number_of_Companies_Form()
    print("Entering Number of Companies page.")
    if request.method == 'POST':
        print("The Number of Companies page form Request method was equal to POST ")
        form = Number_of_Companies_Form(request.POST)
        if form.is_valid():
            #print(form)
            print("The Number of Companies page form is valid Successfully")
            NumberOfCompanies_Integer = form.cleaned_data.get('NumberOfCompanies')
            return redirect('List_of_Companies')
    return render(request, 'FirstPage/Number_of_Companies.html', {'form':form})
@login_required(login_url = 'Home')
def List_of_Companies(request):
    context = {}
    return render(request, 'FirstPage/List_of_Companies.html')
