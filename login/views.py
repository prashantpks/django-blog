from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user_login = auth.authenticate(username = username, password = password)

        if user_login is not None:
            auth.login(request,user_login)
            return redirect('home')
        else:
            messages.error(request,'Invalid Email/Password!')
            return redirect('login')
        
    return render(request,'login/login.html')


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.error(request,'Username already exists!')
                return redirect('signup')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request,'Email address already exists!')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(first_name =firstname, last_name = lastname, email = email, username = username, password = password)
                    auth.login(request,user)
                    messages.success(request,'You are now logged in!')
                    return redirect('home')
                    # if want to redirect to login page after registration
                    '''
                    user.save()
                    messages.success(request,'You are registered successfully')
                    return redirect('login')
                    '''
        else:
            messages.error(request,'Password do not match!')
            return redirect('signup')

    return render(request,'login/signup.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    
    return redirect('home')
