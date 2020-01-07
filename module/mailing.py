# This is a Module for sending Emails

import smtplib
import json
import os

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
        self.receivers = ["receivers"]



        # smtplib.SMTP( [host [, port [, local_hostname]]] )
        self.server = smtplib.SMTP_SSL(self.host, self.port)
        self.server.ehlo()
        self.server.login(self.user, self.password)

    def send_without_file(self):
        try:
            self.server.sendmail(self.user, self.receivers, "Hello 123")
        except:
            print("Somthing went wron by sending a Email")


if __name__ == '__main__':
    email = Mail()


