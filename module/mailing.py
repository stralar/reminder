# This is a Module for sending Emails

import smtplib
import json
import os
import sys

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
        self.receivers = data["receivers"]

    def send_without_file(self, msg):

        try:
            # smtplib.SMTP( [host [, port [, local_hostname]]] )
            self.server = smtplib.SMTP_SSL(self.host, self.port)

            self.server.ehlo()
            self.server.login(self.user, self.password)

            self.server.sendmail(self.user, self.receivers, msg)
            self.server.close()
            pass
        except:
            e = sys.exc_info()[0]
            print("Unexpected error in email sending: " + str(e))
            raise

if __name__ == '__main__':

    email = Mail()

    email.send_without_file("This is a message")


