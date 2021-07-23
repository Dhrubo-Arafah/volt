from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Mentor


class UserCreation(UserCreationForm):
    class Meta:
        model = User
        # fields='__all__'
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class MentorCreationForm(ModelForm):
    class Meta:
        model = Mentor
        exclude = ('user', 'date_joined', 'is_approved')
