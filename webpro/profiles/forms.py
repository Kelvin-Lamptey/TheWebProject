from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Expert

class UserRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.Role.choices)
    
    # Common fields
    bio = forms.CharField(widget=forms.Textarea, required=False)
    profile_picture = forms.ImageField(required=False)

    # Student fields
    programme = forms.CharField(required=False)
    school = forms.CharField(required=False)
    student_courses = forms.CharField(required=False)

    # Expert fields
    programme_of_expertise = forms.CharField(required=False)
    years_of_experience = forms.IntegerField(required=False)
    expert_courses = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role', 'bio', 'profile_picture')

    def save(self, commit=True):
        user = super().save(commit=True)
        
        if user.role == User.Role.STUDENT:
            Student.objects.create(
                user=user,
                programme=self.cleaned_data.get('programme'),
                school=self.cleaned_data.get('school'),
                courses=self.cleaned_data.get('student_courses')
            )
        else:
            Expert.objects.create(
                user=user,
                programme_of_expertise=self.cleaned_data.get('programme_of_expertise'),
                years_of_experience=self.cleaned_data.get('years_of_experience') or 0,
                courses=self.cleaned_data.get('expert_courses')
            )
        
        return user
