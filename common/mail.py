
from django.core.mail import send_mail as dj_send_mail

def my_send_email(title,massage,receiver):
    print('-----start_send_email-----')
    dj_send_mail(
        subject=title,
        message="",
        html_message=massage,
        from_email=receiver[0],
        recipient_list=receiver)
    print('-----finish_send_email-----')