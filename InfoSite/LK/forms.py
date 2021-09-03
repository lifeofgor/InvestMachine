from django import forms
from django.contrib.auth.models import User

from .models import Profile, Lkpage


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))



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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'telegram', 'VK')


class LkpageForm(forms.ModelForm):
    class Meta:
        model = Lkpage
        fields = ('img_page', 'text_page', 'title_page', 'preview_page', 'data_page')

User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

