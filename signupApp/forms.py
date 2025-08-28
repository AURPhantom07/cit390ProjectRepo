from django import forms
from signupApp.models import RegisterCourse

class RegisterCourseForm(forms.ModelForm):
    #specify the model and the fields of the model that will show up on the form
    class Meta:
       model = RegisterCourse
       fields = ['studentID','firstName','lastName']
