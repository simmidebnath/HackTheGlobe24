from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    create_rule_form = forms.BooleanField(label='hidden', widget=forms.HiddenInput, initial=True)

    SKILLS_CHOICES = [
        ('programming', 'Programming'),
        ('IT', 'Information Technology'),
        ('electrician', 'Electrician'),
        ('plumbing', 'Plumbing'),
    ]

    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.Textarea)
    skills = forms.ChoiceField(choices=SKILLS_CHOICES)
    experience = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = UserProfile
        fields = ['full_name', 'email', 'phone', 'address', 'skills', 'experience']
