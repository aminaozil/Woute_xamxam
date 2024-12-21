from django import forms 
from django.contrib.auth.forms import UserCreationForm
    
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label="MOT DE PASSE", widget=forms.PasswordInput(
                                             attrs={
                                                 "class":"block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-[#4a355b] focus:border-[#4a355b] dark:bg-[#4a355b] dark:border-[#4a355b] dark:placeholder-gray-400 dark:text-white dark:focus:ring-[#4a355b] dark:focus:border-[#4a355b]"
                                                 }))
    password2 = forms.CharField(label="CONFIRMATION", widget=forms.PasswordInput(
                                             attrs={
                                                 "class":"block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-[#4a355b] focus:border-[#4a355b] dark:bg-[#4a355b] dark:border-[#4a355b] dark:placeholder-gray-400 dark:text-white dark:focus:ring-[#4a355b] dark:focus:border-[#4a355b]"
                                                 }))

class Meta(UserCreationForm.Meta):
    fields = UserCreationForm.Meta.fields + ("password1", "password2")