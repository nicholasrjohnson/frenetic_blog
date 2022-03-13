from django import forms
from .models import Author
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Layout
from crispy_forms.bootstrap import FormActions, Div, Field 
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = Author
        fields = ('email', 'name', 'phone', 'date_of_birth', 'photo', 'password', 'bio', 'signature')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Please confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Author
        fields = ('email', 'name', 'phone', 'date_of_birth', 'photo', 'bio', 'signature', 'is_staff', 'is_superuser')
    
    def clean_passwordConfirm(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password1
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Author
        fields = ('email', 'name', 'phone', 'date_of_birth', 'photo', 'password', 'bio', 'signature', 'is_active', 'is_superuser')
    
    def clean_password(self):
        return self.initial["password"]