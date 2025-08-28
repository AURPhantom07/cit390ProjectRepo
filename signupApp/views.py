from django.shortcuts import render, get_object_or_404
from .models import RegisterCourse
from .forms import RegisterCourseForm

def registerCourse(request):
 regis = RegisterCourse.objects.all()
 form = RegisterCourseForm()
 #context['form'] = form
 
 #take data from form and save it to the model
 if request.method == 'POST':
   if 'save' in request.POST:
      form = RegisterCourseForm(request.POST)
      if form.is_valid():         
         form.save()      

 return render(request,'signupApp/register.html',{'form':form, 'regis':regis})