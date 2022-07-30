from django.core.mail import send_mail


def send_register_email(email):
    send_mail(
        'Retreat',
        'Hi your teacher add you to class in my site',
        'test@test.com',
        [email, ],
        fail_silently=False
    )
