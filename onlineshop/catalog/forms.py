from django import forms
from .models import Feedbacks, Orders
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class FeedbacksForm(forms.ModelForm):
    class Meta():
        model = Feedbacks
        fields = ['name', 'feedback_text', 'ratingcomment']

class LoginForm(forms.Form):
    class Meta():
        model = User
        fields = ['username', 'password']

class RegisterForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['first_name', 'username', 'email', 'password']

class OrdersForm(forms.ModelForm):
    class Meta():
        model = Orders
        fields = ['order_owner']