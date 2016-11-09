from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    sender = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    jerk = forms.BooleanField(required=False)

    def send_email(self):
        sender = self.cleaned_data['sender']
        message = self.cleaned_data['message']
        jerk = self.cleaned_data['jerk']
        subject = "Contact Form Submission"
        body = """Hey Connor, you got a new contact form submission:
        From: {}
        Message: {}
        Are they a jerk: {} """.format(sender,message,jerk)
        recipient_list = ['connor.redmond@gmail.com']

        send_mail(subject, body, "connorthrowaway1@gmail.com",recipient_list)
