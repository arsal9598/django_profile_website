from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ContactForm(forms.Form):
    your_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-contant-form'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
