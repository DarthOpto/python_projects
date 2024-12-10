from smtplib import SMTP_SSL as SMTP


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "curtis.salisbury@gmail.com"
    password = "lgovidjtlsdisajc"
    receiver = "curtis.salisbury@gmail.com"

    with SMTP(host, port):
        server = SMTP(host)
        server.login(username, password)
        server.sendmail(username, receiver, message)

