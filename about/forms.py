from django import forms


class CollaborateForm(forms.Form):
    """
    Simple form for collaboration requests. This is a plain
    Form (not a ModelForm) because the CollaborateRequest model
    was removed.
    """
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)