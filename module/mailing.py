# This is a Module for sending Emails

import smtplib
import json
import os
import sys


class Mail:
    def __init__(self):
        # load config
        with open(os.path.dirname(os.path.abspath(__file__)) + '/config/mail_client.json') as json_data_file:
            data = json.load(json_data_file)

        print(data)


        self.user = data["user"]
        self.password = data["password"]
        self.host = data["host"]
        self.port = data["port"]
        self.receivers = data["receivers"]





    def send_without_file(self):

        try:
            # smtplib.SMTP( [host [, port [, local_hostname]]] )
            self.server = smtplib.SMTP_SSL(self.host, self.port)

            # self.server = smtplib.SMTP(self.host, self.port)
            # self.server.starttls()

            self.server.ehlo()
            self.server.login(self.user, self.password)

            self.server.sendmail(self.user, "larsstratmann@gmx.de", "Hello 123")
            self.server.close()
            pass
        except:
            e = sys.exc_info()[0]
            print("Unexpected error in email sending: " + e)
            raise


if __name__ == '__main__':
    email = Mail()

    email.send_without_file()


