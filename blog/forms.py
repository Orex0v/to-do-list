from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Post


class PostForm(forms.ModelForm):
    CHOICES=[(True,'Выполнено'), (False, 'В работе')]
    deadline = forms.DateField(widget=forms.SelectDateWidget)
    compile_post = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Post
        fields = ('title', 'text', 'deadline', 'compile_post')
    
class CompliteForm(forms.ModelForm):
    # compile_post = True
    class Meta:
        model = Post
        fields = ()

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)
    phone_number = forms.CharField(max_length=12)
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2', )