from django import forms

from carcollection.profile_app.models import ProfileModel


class BaseProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = ProfileModel
        fields = ('username', 'email', 'age', 'password')


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    pass
    class Meta:
        model = ProfileModel
        fields = '__all__'
