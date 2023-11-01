from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
		path("logout", views.custom_logout, name="logout"),
		path("login", views.custom_login, name="login"),
		path("signup", views.signup, name="signup"),
		path("question", views.question, name="question"),
		path("question/<int:pk>", views.question, name="question"),
		path("answer", views.answer, name="answer"),
		path("answer/<int:pk>", views.answer, name="answer"),
		path("vote/<int:pk>", views.vote, name="vote"),
		path("", views.home, name="home"),
]
