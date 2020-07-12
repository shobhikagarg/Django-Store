from django import forms
from .models import Stock

class StockCreateForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields='__all__'

class StockSearchForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['category','item_name']
        labels = {'category': 'Select the Category'}
        help_text = {'item_name': 'Enter name of the item'}
        widgets={'item_name':forms.TextInput}

def clean_category(self):
    category=self.cleaned_data['category']
    if not category:
        raise forms.ValidationError('This is required')
    return category

class UserCreationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    password_repeat = forms.CharField()

class IssueForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['issue_quantity', 'issue_to']


class ReceiveForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['received_quantity', 'receive_by']
