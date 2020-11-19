from django.urls import path

from users  import views

urlpatterns = [
    path('login/', views.loginPage, name = "login"),
    path('register/', views.register, name = "register"),
    path('logout/', views.logout_user, name = "logout"),

]