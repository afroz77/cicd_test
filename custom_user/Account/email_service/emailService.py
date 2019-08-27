from django.contrib.sites.shortcuts import get_current_site     # import for getting the current site
from django.template.loader import render_to_string         # this is for creating the link for activation
from django.core.mail import EmailMessage                   # this for send the email


class emailService:
    def send_email(self, request, user, email, note_title):
        current_site = get_current_site(request)
        mail_subject = "Activate Your Account"
        message = render_to_string("Fundooapp/collaborate.html", {
            'user': user,
            'domain': current_site.domain,
            'title': note_title,
        })
        to_email = email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

