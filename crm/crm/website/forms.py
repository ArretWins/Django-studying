from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SingUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=25, required=True)
    last_name = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]
        

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"w-full mt-2 py-4 px-6 rounded-xl text-black focus:outline-none focus:border-cyan-500 focus:ring-4 focus:ring-cyan-500"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"w-full mt-2 py-4 px-6 rounded-xl text-black focus:outline-none focus:border-cyan-500 focus:ring-4 focus:ring-cyan-500"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"w-full mt-2 py-4 px-6 rounded-xl text-black focus:outline-none focus:border-cyan-500 focus:ring-4 focus:ring-cyan-500"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"w-full mt-2 py-4 px-6 rounded-xl text-black focus:outline-none focus:border-cyan-500 focus:ring-4 focus:ring-cyan-500"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"w-full mt-2 py-4 px-6 rounded-xl text-black focus:outline-none focus:border-cyan-500 focus:ring-4 focus:ring-cyan-500"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"w-full mt-2 py-4 px-6 rounded-xl text-black focus:outline-none focus:border-cyan-500 focus:ring-4 focus:ring-cyan-500"}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"w-full mt-2 py-4 px-6 rounded-xl text-black focus:outline-none focus:border-cyan-500 focus:ring-4 focus:ring-cyan-500"}), label="")
    
    class Meta:
        model = Record
        exclude = ("user",)