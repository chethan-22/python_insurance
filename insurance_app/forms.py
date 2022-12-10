from django import forms
from .models import Insurances, InsuredMembers, CustAddress


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurances
        fields = '__all__'

        widgets = {
            "cust_key": forms.TextInput()
        }



class InsuredMembersForm(forms.ModelForm):
    class Meta:
        model = InsuredMembers
        fields = '__all__'

class AddressForm(forms.ModelForm):
    class Meta:
        model = CustAddress
        fields = '__all__'

        widgets = {
            "cust":forms.TextInput()
        }


