from django import forms


class ContactUserForm(forms.Form):
    contact_name = forms.CharField(validators=[], label='', max_length=200, widget=forms.TextInput(attrs={
        'placeholder': '  Name ',
        'label': 'Name',
        'class': ' form-control     span',
    }))
    contact_email = forms.EmailField(max_length=200, label='', widget=forms.EmailInput(attrs={
        'placeholder': ' Email ',
        'class': 'form-control    span',

    }))
    contact_subject = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={
        'placeholder': 'Subject ',
        'class': 'form-control   ',
    }))
    contact_message = forms.CharField(label='', widget=forms.Textarea(attrs={
        'placeholder': ' Message ',
        'class': ' ',
        'cols': '40',
        'style': 'min-height: 30px!important;height:20vh',
        'rows': '10'
    }))
    to_email = forms.EmailField(widget=forms.HiddenInput(attrs={
        'placeholder': ' Email ',
        'class': 'form-control   d-none',
        'style': {'margin-bottom': '0rem'}

    }))

    def clean_email(self):
        email_passed = self.cleaned_data.get('email')
        email_req = 'mmm'
        if email_passed != email_req:
            return forms.ValidationError("Not a valig email pls try again")
        return email_passed


class ContactAdminForm(forms.Form):
    contact_name = forms.CharField(validators=[], label='', max_length=50, widget=forms.TextInput(attrs={
        'placeholder': '  Name ',
        'label': 'Name',
        'class': ' form-control     span',
    }))
    contact_email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'placeholder': ' Email ',
        'class': 'form-control    span',

    }))
    contact_subject = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs={
        'placeholder': 'Subject ',
        'class': 'form-control   ',
    }))
    contact_message = forms.CharField(max_length=1000, label='', widget=forms.Textarea(attrs={
        'placeholder': ' Content ',
        'class': 'md-textarea form-control    ',
        'rows': '5',
        'cols': '20',
    }))

    def clean_email(self):
        email_passed = self.cleaned_data.get('email')
        email_req = 'mmm'
        if email_passed != email_req:
            return forms.ValidationError("Not a valig email pls try again")
        return email_passed
