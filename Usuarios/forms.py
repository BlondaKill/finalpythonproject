from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class Usuario_Form(UserCreationForm):
    avatar = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nombre de usuario ya está en uso.')

        return cleaned_data

    def save(self, commit=True):
        user = super(Usuario_Form, self).save(commit=False)
        avatar_data = self.cleaned_data.get('avatar')

        if commit:
            user.save()

        if avatar_data:
            avatar = Avatar(User=user, Imagen=avatar_data)
            if commit:
                avatar.save()

        return user


class Usuario_Form_2(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name' , 'last_name', 'username', 'email', 'password', 'avatar']

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        avatar_data = self.cleaned_data.get('avatar')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        if avatar_data:
            avatar, created = Avatar.objects.get_or_create(User=user)
            avatar.Imagen = avatar_data
            if commit:
                avatar.save()

        return user




