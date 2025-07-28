from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]
        labels = {
            'username': 'Имя пользователя',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }


class UserUpdateForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
        required=False
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Введенные пароли не совпадают")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password1"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput
    )
