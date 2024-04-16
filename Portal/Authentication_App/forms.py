from django.forms import ModelForm,Textarea
from Authentication_App.models import User_Profile
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User

# Create your models here.

class ProfilePicForm(ModelForm):
    class Meta:
        model = User_Profile
        fields = ['profile_pic']
      

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']



class UpdateProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']