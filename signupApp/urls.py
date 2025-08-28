from django.urls import path
from . import views

app_name = 'signupApp'
urlpatterns = [
 # registerCourse views
 path('', views.registerCourse, name='registerCourse'),
 #as_view() is needed for class based views, name is the url path on the browser; 127.0.0.1:80/registerCourse
 #'' means this is also the home page; if nothing specified after the IP:port
]

