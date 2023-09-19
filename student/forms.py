from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #fields = '__all__' luam toate fieldurile din model si le afisam in ordinea scrisa in model
        fields = ['first_name', 'last_name', 'age', 'email', 'description',  'active',
                  'start_date', 'end_date', 'gender', "trainer", "profile"] # specificam fieldurile dorite in formular si ordinea lor

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your descrption',
                                           'rows': 3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # type -> datetime-local
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # type -> datetime-local
            'gender': Select(attrs={'class': 'form-select'}),
            'trainer': Select(attrs={'class': 'form-select'})
        }



    def clean(self):
        cleaned_data = self.cleaned_data # se genereaza inun dictionar cu datele completate in formular

        # o unicitate pt adresa de email
        get_email = cleaned_data.get('email') # cleaned_data['email']
        check_email = Student.objects.filter(email=get_email)
        if check_email:
            msg = 'Exista emailul deja'
            self._errors['email'] = self.error_class([msg])

        # verificare startdate > endate
        get_start_date = cleaned_data.get('start_date')
        get_end_date = cleaned_data.get('end_date')

        if get_start_date > get_end_date:
            msg = 'Start date ul este mai mare decat end date'
            self._errors['start_date'] = self.error_class([msg])

        return cleaned_data

# Class Meta intr-un proiect Django  este folosit pentru
# a defini metadatele asociate cu un formular

# Aceste metadate includ informatii despre modelul (Student)
# legat de formularul, campurile care trebuiesc sa apara in formular
# si pe care le putem customiza, adaugand clase de CSS, placeholder etc.


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        #fields = '__all__' luam toate fieldurile din model si le afisam in ordinea scrisa in model
        fields = ['first_name', 'last_name', 'age', 'email', 'description',  'active',
                  'start_date', 'end_date', 'gender', "trainer", "profile"] # specificam fieldurile dorite in formular si ordinea lor

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your descrption',
                                           'rows': 3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # type -> datetime-local
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # type -> datetime-local
            'gender': Select(attrs={'class': 'form-select'}),
            'trainer': Select(attrs={'class': 'form-select'})
        }

