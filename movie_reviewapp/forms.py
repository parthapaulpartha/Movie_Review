from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import comment_movie_review, contact

# -------- Registration ----------
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

# -------- Login ----------
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

# -------- EditProfile ----------
class EditprofileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]

# ------- Comment Movie Review ---------
class CommentMovieReviewForm(forms.ModelForm):
    class Meta:
        model = comment_movie_review
        fields = [
            'comment_review',
            'rating',
        ]
        widgets = {'rating': TextInput(attrs={'placeholder': 'Enter your rating for this movie (0/10)'})}

# ------- Contact ---------
class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = [
            'email',
            'message'
        ]
        widgets = {'email': TextInput(attrs={'placeholder': 'Enter your email'})}