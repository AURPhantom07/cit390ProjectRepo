from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('signupApp/', include('signupApp.urls', namespace:'signupApp'))
    path('', include('signupApp.urls', namespace='signupApp')),
]

# path('admin/', admin.site.urls), Routes requests to /admin/ to Django’s admin interface.
# Django’s admin site is a powerful, built-in tool that provides: A graphical interface for #managing your database objects. Easy tools for creating, reading, updating, and deleting #entries - known as CRUD operations.
# path('', include('signupApp.urls', namespace='signupApp')), This includes all the URL #patterns from the signupApp.urls module. The empty string '' means it's the root URL - so #any request that doesn't start with another path will be sent to this app (e.g. http://127.0.0.1:8000/). If we use “path('signupApp/', include('signupApp.urls', namespace='signupApp')),” then you must include this path to visit the app (e.g. http://127.0.0.1:8000/'signupApp/)
"""The namespace='signupApp' allows for namespaced URL reversing, which is useful in templates or views to avoid naming collisions - especially useful when different apps in the same project have routes with similar names. That means any URL from signupApp.urls can now be reversed (i.e. generated dynamically) using this namespace. Assuming signupApp/urls.py contains:

…………………………………………………………
app_name = 'signupApp'
urlpatterns = [
    path('register/', views.register, name='register'),
]
……………………………………………………………..
Then in your template, you'd reference the register URL like this: 
{% url 'signupApp:register' %}



E.g. shopApp/register, signupApp/register app urls in the same project. We can use the namespace to identify exactly which app in the html;  <a href="{% url 'signupApp:register' %}">Sign Up</a> where register/ is the url """