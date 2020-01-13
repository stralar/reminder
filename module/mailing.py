# This is a Module for sending Emails

import smtplib
import json
import os
import sys

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


config_File = "mail_client_real.json"
#config_File = "mail_client.json"


class Mail:
    def __init__(self):
        # load config
        with open(os.path.dirname(os.path.abspath(__file__)) + '/config/' + config_File) as json_data_file:
            data = json.load(json_data_file)

        print(data)

        self.user = data["user"]
        self.password = data["password"]
        self.host = data["host"]
        self.port = data["port"]

        try:
            self.server = smtplib.SMTP_SSL(self.host, self.port)

            self.server.ehlo()
            self.server.login(self.user, self.password)
        except:
            print("SMTP Client could not start")
            raise

    def shutdown_smtp(self):
        self.server.close()

    def send_without_file(self, receivers, subject, mainText):

        try:
            print("Send mail to: " + str(receivers))
            self.server.sendmail(self.user, receivers, mainText)
            pass
        except:
            e = sys.exc_info()[0]
            print("Unexpected error in email sending: " + str(e))
            raise


    def send_with_file(self, receivers, subject, mainText, file, filename):

        msg = MIMEMultipart()
        msg['From'] = self.user
        msg['To'] = receivers
        msg['Subject'] = subject
        msg.attach(MIMEText(mainText, 'plain'))

        attachment = file
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename=" + str(filename) + ".ics")

        msg.attach(part)

        text = msg.as_string()

        try:
            print("Send mail to: " + str(receivers))
            self.server.sendmail(self.user, receivers, text)
            pass
        except:
            e = sys.exc_info()[0]
            print("Unexpected error in email sending: " + str(e))
            raise



if __name__ == '__main__':

    email = Mail()

    email.send_without_file("This is a message")


