from .models import EmailAccount, EmailMessage
import imaplib
import email

def fetch_emails():
    accounts = EmailAccount.objects.all()
    for account in accounts:
        mail = imaplib.IMAP4_SSL('imap.' + account.email.split('@')[1])
        mail.login(account.email, account.password)
        mail.select('inbox')

        status, data = mail.search(None, 'ALL')
        mail_ids = data[0].split()
        for i, mail_id in enumerate(mail_ids):
            status, data = mail.fetch(mail_id, '(RFC822)')
            msg = email.message_from_bytes(data[0][1])
            subject = msg['subject']
            sent_date = msg['date']
            received_date = msg['date']  # Это можно заменить на правильное поле
            description = msg.get_payload()
            attachments = []  # Логика для обработки вложений

            EmailMessage.objects.create(
                email_account=account,
                subject=subject,
                sent_date=sent_date,
                received_date=received_date,
                description=description,
                attachments=attachments
            )
            # Отправка прогресса через WebSocket
            # ...
