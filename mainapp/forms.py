from django import forms
class contact_usform(forms.Form):
    subject=forms.EmailField(max_length=100)
    message=forms.CharField(widget=forms.Textarea)
    to_email=forms.EmailField(label="Recipient Email",max_length=100)