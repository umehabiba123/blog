from django.shortcuts import render,redirect,HttpResponseRedirect, HttpResponse
from .models import Categorie , Blog
from .forms import Create_blog_form, SignUpForm, LoginForm
from django.core.files.storage import FileSystemStorage

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
# Create your views here.
def catogories_page(request):
   catogry = Categorie.objects.all()
   return render(request,"category_page.html",{"Category":catogry})


def blogs(request):
   catogry = Categorie.objects.all()
   blog = Blog.objects.all()
   return render(request,"Blogger_blogs.html",{"Category":catogry,"blogs":blog})


def create_blog(request):
    form = Create_blog_form(request.POST or None, request.FILES or None)
    if form.is_valid():   
        form.save()
        return redirect("/blog/")
    return render(request, "create_blog.html", {"form": form})


def home(request):
    blog = Blog.objects.all()
    return render(request,"home.html",{"blog":blog})


def read_more(request, id):
    blog = Blog.objects.get(pk=id)
    return render(request,"read_more.html",{"blog" : blog})


def delete(request,id):
    blog = Blog.objects.get(pk = id)
    blog.delete()
    return redirect("/")


def edit_blog(request,id):
    blog = Blog.objects.get(pk = id)
    if request.method == "POST":
        blog.title = request.POST.get("title")
        blog.description = request.POST.get("description")
        blog.author = request.POST.get("author")
        blog.tags = request.POST.get("tags")
        blog.image = request.FILES["image"]
        blog.save()
        return redirect("/blog/")
    return render(request, "edit_blog.html", {"blog": blog})

def Category(request,id): 
    Category  = Categorie.objects.get(pk=id)
    get_category = Blog.objects.filter(category=Category)
    return render(request, "blog_categories.html",{"category" : get_category })


# ************************************Login Logout Signup ********************************************




def user_signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        if request.method == 'POST':
            
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Congratulation !! You have become an author')
                form.save()
                # user = form.save()
                # group = Group.objects.get(name='Author')
                # user.groups.add(group)
                return HttpResponseRedirect('/')
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    
    




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
                    return HttpResponseRedirect('/home/')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/home/')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def middle(request):
    a = 10/0
    return HttpResponse("Finally i make my middleware")

# def dashboard(request):
#     if request.user.is_authenticated:
#         posts = Blog.objects.all()
#         user = request.user
#         full_name = user.get_full_name()
#         groups = user.groups.all()
#         return render(request, 'dashboard.html', {'posts': posts, 'full_name': full_name, 'groups': groups})
#     else:
#         return HttpResponseRedirect('/login/')
