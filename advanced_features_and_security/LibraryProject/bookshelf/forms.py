from django import forms

class ExampleForm(forms.Form):
    # Define the form fields here
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
