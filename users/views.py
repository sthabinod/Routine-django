from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required




def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            return redirect('login')
            form.save()
            messages.success(request, 'Account created successfully')
        else:
            messages.error(request,'Account is not created successfully')

    context = {'form':form}
    return render(request,"users/register.html",context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is None:
            messages.info(request, "Username or password is incorrect.")
            return render(request, 'users/login.html')
        else:
            login(request, user)
            return redirect('index')

    return render(request,"users/login.html")

@login_required(login_url='login')
def logout_user(request):
    # messages.add_message(request, CRITICAL, 'A serious error occurred.')
    messages.info(request,'You are logged out from the device')
    return redirect('login')