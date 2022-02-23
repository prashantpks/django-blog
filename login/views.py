from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserProfileChange, ProfilePic

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
                    pic = ProfilePic();
                    user.save()
                    # Add default profile pic to user account
                    profilePic = pic.save(commit = False)
                    profilePic.user = user
                    profilePic.save()
                    auth.login(request,user)
                    messages.success(request,'You are now logged in!')
                    return redirect('home')
                    # if want to redirect to login page after registration
                    '''
                    
                    messages.success(request,'You are registered successfully')
                    return redirect('login')
                    '''
        else:
            messages.error(request,'Password do not match!')
            return redirect('signup')

    return render(request,'login/signup.html')

@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    
    return redirect('home')

@login_required
def profile(request):
    return render(request,'login/profile.html')

@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance = current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance = current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance = current_user)
            messages.success(request,'Profile Info Updated!')
            return redirect('profile')

        else:
            messages.error((request,'Invalid Data Entered!'))
            redirect('change_profile')
    
    data = {
        'form':form,
    }

    return render(request,'login/change_profile.html',data)

@login_required
def pass_change(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user,data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Changed Successfully!')
            
    
    data = {
        'form':form,
    }
    return render(request,'login/pass_change.html', data)


@login_required
def add_pro_pic(request):
    form = ProfilePic()

    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        print(form.POST);
        print(request.FILES);
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return redirect('profile')

    data = {
        'form':form,
    }
    return render(request,'login/add_pro_pic.html',data)


@login_required
def change_pro_pic(request):
    form = ProfilePic(instance = request.user.user_profile)

    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES,instance = request.user.user_profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Pic updated successfully!')
            return redirect('profile')
    data = {
        'form': form,
    }
    return render(request,'login/add_pro_pic.html',data)