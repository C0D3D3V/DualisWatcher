import smtplib
from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid

class MailShooter:
    def __init__(sef, sender: str, smtp_server_host: str, smtp_server_port: int, username: str, password: str):
        sef.sender = sender
        sef.smtp_server_host = smtp_server_host
        sef.smtp_server_port = smtp_server_port
        sef.username = username
        sef.password = password

    def send(self, target: str, subject: str, html_content_with_cids: str, inline_png_cids_filenames: {str : str}):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = target

        msg.set_content('')

        msg.add_alternative(
            html_content_with_cids, subtype='html'
        )

        for png_cid in inline_png_cids_filenames:
            with open(inline_png_cids_filenames[png_cid], 'rb') as png_file:
                file_contents = png_file.read()
                msg.get_payload()[1].add_related(file_contents, 'image', 'png', cid=png_cid)

        with smtplib.SMTP(self.smtp_server_host, self.smtp_server_port) as smtp_connection:
            smtp_connection.starttls()
            smtp_connection.login(self.username, self.password)
            smtp_connection.send_message(msg)
