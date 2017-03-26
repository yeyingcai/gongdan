from django import forms

class add_order(forms.Form):
    fo_type = forms.IntegerField()
    fo_title = forms.IntegerField()
    fo_text = forms.IntegerField()
    fo_user = forms.IntegerField()