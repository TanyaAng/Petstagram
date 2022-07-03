from django import forms

from petstagram.main.models import Profile
from petstagram.main.views.helpers import BootstrapFormMixin


class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
            'picture': forms.TextInput(
                attrs={'placeholder': 'Enter URL'}),
        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW
        self.fields['date_of_birth'].input_type = 'date'
        # self.fields['gender'].initial=Profile.DO_NOT_SHOW

    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
            'picture': forms.TextInput(
                attrs={'placeholder': 'Enter URL'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter description', 'rows': 3}, ),
            'date_of_birth': forms.DateInput(attrs={'min': '1920-01-01', })
        }


class DeleteProfileForm(forms.ModelForm):
    # overwrite save method
    def save(self,commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields=()
        # same as
        # exclude = ('first_name', 'last_name', 'picture', 'date_of_birth', 'description', 'gender', 'email')
