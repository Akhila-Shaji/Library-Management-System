from django import forms
from .models import *
from django.contrib.auth.models import User

class Student_Registration(forms.ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput)
    cpassword = forms.CharField(label='confirm password', widget=forms.PasswordInput)
    phone = forms.IntegerField(label='phone number', widget=forms.TextInput)
    roll_no = forms.IntegerField(label='Roll number', widget=forms.TextInput)
    register_id = forms.CharField(label='Register id', widget=forms.TextInput)
    college_name=forms.CharField(label='college name',widget=forms.TextInput)
    my_choice=(
        ('cse','CSE'),
        ('eee','EEE'),
        ('mech','Mechanical'),
        ('civil','Civil')
    )
    department=forms.ChoiceField(label='Department',choices=my_choice)
    class Meta:
        model=User
        fields = ['username','first_name','last_name','phone','email','password','cpassword','department','roll_no','register_id','college_name']


class book_detail_form(forms.ModelForm):
    class Meta:
        model = Library_Book_Details
        fields =['book_name','book_image','Author','book_id','description','available_copies']


class Editprofile(forms.ModelForm):
    my_choice = (
        ('cse', 'CSE'),
        ('eee', 'EEE'),
        ('mech', 'Mechanical'),
        ('civil', 'Civil')
    )
    department = forms.ChoiceField(label='Deaprtment', choices=my_choice)
    phone = forms.IntegerField(label='phone number', widget=forms.TextInput)
    roll_no = forms.IntegerField(label='Roll number', widget=forms.TextInput)
    register_id = forms.CharField(label='Register id', widget=forms.TextInput)
    college_name = forms.CharField(label='college name', widget=forms.TextInput)
    class Meta:
        model=User
        fields = ['first_name','roll_no','email','department','phone','register_id','college_name']