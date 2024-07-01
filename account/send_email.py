from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_confirmation_email(email, code):
    activation_url = f'http://34.171.36.251/api/account/activate/?u={code}'
    context = {'activation_url': activation_url}
    subject = 'Здравствуйте, активируйте ваш аккаунт!'
    html_message = render_to_string('account/activate.html', context)
    plain_message = strip_tags(html_message)

    send_mail(
        subject, 
        plain_message, 
        'ainazikbaltabaeva@gmail.com',
        [email], 
        html_message=html_message, 
        fail_silently=html_message
    )

def send_confirmation_password(email, code):
    activation_url = f'http://34.171.36.251/api/account/reset_password/confirm/?u={code}'
    context = {'activation_url': activation_url}
    subject = 'Здравствуйте, подвердите изменение пароля!'
    html_message = render_to_string('account/new_password.html', context)
    plain_message = strip_tags(html_message)

    send_mail(
        subject, 
        plain_message, 
        'ainazikbaltabaeva@gmail.com',
        [email], 
        html_message=html_message, 
        fail_silently=html_message
    )