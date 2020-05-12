from django.urls import path,include
from django.contrib.auth import views as auth_views
from ziff.views import book, motivation, pre, note
urlpatterns = [
	path('', book),
	path('motivation/',motivation),
	path('previous/', pre),
	path('notes/', note),
]
