from django import forms

class HeyForm(forms.Form):
    name = forms.CharField()

class Age(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()
    
class BadBurger(forms.Form):
    burger = forms.IntegerField()
    drinks = forms.IntegerField()
    fries = forms.IntegerField()
    
