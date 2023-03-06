#imports for forms.py 
from django import forms
from .models import * # import all of your models

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = "__all__" 


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = "__all__" 
        widgets = {
            "name": forms.TextInput(attrs={'placeholder':'John Doe'}),
            "cardnumber": forms.TextInput(attrs={'placeholder':'1234 1234 1234 1234'}),
            "cvv": forms.TextInput(attrs={'placeholder':'CVV'}),
            "address1": forms.TextInput(attrs={'placeholder':'15 Bakers Street'}),
            "address2": forms.TextInput(attrs={'placeholder':'Glasnevin'}),
            "city": forms.TextInput(attrs={'placeholder':'Dublin'}),
            "eircode": forms.TextInput(attrs={'placeholder':'A65F4E2'}),
        }
