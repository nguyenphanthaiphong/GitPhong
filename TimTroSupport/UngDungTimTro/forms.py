from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Property, Image


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'location', 'category', 'facilities']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_url', 'is_main']


class PropertyImageForm(forms.Form):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))