from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login_view
        fields = ('username','password1','password2',)
        
class DesignerRegister(forms.ModelForm):
    
    class Meta:
        model = Designers
        fields = "__all__"
        exclude = ("user","status")

class UsersRegister(forms.ModelForm):

    class Meta:
        model = users
        fields = "__all__"
        exclude = ("user",)
class DesignTaskForm(forms.ModelForm):
    class Meta:
        model = DesignTask
        fields = ['title', 'description']

class DesignSubmissionForm(forms.ModelForm):
    class Meta:
        model = DesignSubmission
        fields = ['design_draft', 'feedback']
class DesignRequestForm(forms.ModelForm):
    class Meta:
        model = DesignRequest
        fields = ['title', 'description', 'image']

class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ['title', 'description', 'image']