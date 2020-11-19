from django.urls import path

from result import views

urlpatterns = [
    path('add/', views.index,name="index"),
    path('view/',views.view_result,name="view-result"),
    path('display/',views.display_result,name="display-result")
]