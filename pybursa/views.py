from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.views.generic.edit import FormView
from django.utils.translation import ugettext_lazy as _
from django.utils import translation

import logging
logger = logging.getLogger(__name__)

class ContactForm(forms.Form):
    email = forms.EmailField(label=_("Email"))
    theme = forms.CharField(label=_("Theme"), max_length=255)
    body = forms.CharField(label=_("Message body"), widget=forms.Textarea)


def contact(request):
    # logger.debug("Logging at DEBUG level")
    # logger.info("Logging at INFO level")
    # logger.warning("Logging at WARNING level")
    # logger.error("Logging at ERROR level")
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            theme = form.cleaned_data['theme']
            body = form.cleaned_data['body']
            
            send_mail(theme, body, email, ['dixon.che@gmail.com'])
            messages.success(request, 'Message was send.')
            return redirect('contact-us')
    else:
        form = ContactForm()
    return render(request, 'contact/form.html', {'form': form})


