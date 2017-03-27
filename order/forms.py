from django import forms

class add_order_forms(forms.Form):
    fo_type = forms.CharField()
    fo_title = forms.CharField()
    fo_text = forms.Textarea()