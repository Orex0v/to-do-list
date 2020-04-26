from django import forms
# from django.forms.widgets import SelectDateWidget
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