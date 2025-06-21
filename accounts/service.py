from django.core.mail import send_mail


def send_email_letter():
    send_mail(
        subject='Django email sinovi',
        message = 'Bu test email',
        from_email='rizayevamm@gmail.com',
        recipient_list=['rizayevamm@gmail.com'],
        fail_silently='False',
        html_message=""" 
        <main> 
            <h1>Xush Kelibsiz</h1> 
            <p>Bu sizning asosiy sahifangiz.</p> 
        </main> 
        """
    )
