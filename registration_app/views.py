from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blogs_application.models import Blog
from django.contrib.auth.models import User, Group


# Create your views here.


def user_signup_form(request):
    form = SignUpForm(request.POST or None ,request.FILES or None)
    if form.is_valid():
        messages.success(request, 'Congratulation !! You have become an author')
        user=form.save()
        group = Group.objects.get(name='Author')
        user.groups.add(group)
        return redirect('/')
       
    return render(request, "signup.html",{"form":form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password =  form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'LoggedIn successfully')
                    return HttpResponse('hellow how are you')
                    # return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponse('hellow how are you')
    #     return HttpResponseRedirect('/dashboard/')

