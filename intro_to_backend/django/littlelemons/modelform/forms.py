from .models import Test, CustomUser
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'
class CustomUserForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Username",
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        label="Email Address"
    )
    password1 = forms.CharField(
        required= True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="Password"
    )
    password2 = forms.CharField(
        required= True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="Confirm Password"
    )


    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = Test
        fields = (
                "username,",
                "password",
                )

