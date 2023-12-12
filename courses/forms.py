from django import forms
from django.forms import TextInput, Textarea, DateInput, NumberInput, Select
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'description',
            'instructor',
            'start_date',
            'active',
            'duration_in_weeks',
            'price',
            'profile'
        ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course title'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter course description'}),
            'instructor': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter instructor'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'duration_in_weeks': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter duration in weeks'}),
            'price': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
        }
# forms.py

from django import forms
from django.forms import TextInput, Textarea, DateInput, NumberInput, Select
from .models import Instructor, Category, Tag, Course, Section, Lecture, Enrollment, Rating

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['user', 'bio']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'bio': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter bio'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tag name'}),
        }

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title', 'course']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter section title'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
        }

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'video_url', 'section']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lecture title'}),
            'video_url': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter video URL'}),
            'section': forms.Select(attrs={'class': 'form-control'}),
        }

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['user', 'course', 'enrolled_at']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'enrolled_at': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['course', 'user', 'rating', 'review']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'rating': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter rating'}),
            'review': Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter review'}),
        }
