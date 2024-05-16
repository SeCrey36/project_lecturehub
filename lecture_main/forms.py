from django import forms
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from ckeditor.widgets import CKEditorWidget

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'description', 'category')
        widgets = {
            'content': CKEditorWidget()
        }
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    

class ChangeUsernameForm(forms.ModelForm):
    new_username = forms.CharField(label='New Username', max_length=150)

    class Meta:
        model = User
        fields = ['new_username']

    def clean_new_username(self):
        new_username = self.cleaned_data.get('new_username')
        if User.objects.filter(username=new_username).exists():
            raise forms.ValidationError("This username is already taken. Please choose a different one.")
        return new_username
    
class ChangePasswordForm(PasswordChangeForm):
    # Пронаследуюсь, чтобы не импортировть формы "с коробки" в views.py
    pass

class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=CKEditorWidget())