from django.urls import path
from .views import blogs,create_blog,home,read_more,delete,edit_blog,catogories_page,Category,user_signup, user_login, user_logout, middle

urlpatterns = [
    path("blog/", blogs,name="blogs" ),
    path("cat_pa/",catogories_page, name="catogories"),
    path("cre/",create_blog,name = "create"),
    path("home/",home, name="home"),
    path("read/<int:id>",read_more, name = "read_more"),
    path("del/<int:id>",delete,name = "delete"),
    path("edit/<int:id>",edit_blog,name = "edit_blog"),
    path("cat/<int:id>",Category,name="Category"),
    path("",user_signup, name="user_signupForm"),
    path("login/", user_login , name="user_login"),
    path('logout/', user_logout, name='user_logout'),
    path('mid/', middle, name="middle")
    # path('dashboard/', dashboard, name='dashboard'),
]