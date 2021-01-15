import smtplib

password = input("Type your account password: ")

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # server.login('kennethnull404@gmail.com', 'Asmerkosen123')
    server.login('kennethnull404@gmail.com', password)

    subject = 'Test sent email with Python'
    body = 'Hey, this is just a test mail'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'kennethnull404@gmail.com',
        'rsolleza7@gmail.com',
        msg
    )

    print('Email Sent success!')
    server.quit()

# send_mail()
if __name__ == "__main__":
    send_mail()