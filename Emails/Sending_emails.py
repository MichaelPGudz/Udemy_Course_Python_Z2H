# smtp-mail.outlook.com
import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp-mail.outlook.com', 465) #587 or 465 port numbers

smtp_object.ehlo()

# smtp_object.quit()
# #SKIP if using SSL with 465
# smtp_object.starttls()
#
email = getpass.getpass("Email: ")
password = getpass.getpass("Password:")

smtp_object.login(email, password)

from_address = email
to_address = email
subject = "Rozpoczęcie pracy"
message = "Hej," \
          "Właśnie rozpoczynam pracę." \
          "Dzięki," \
          "" \
          "Andrzej"
msg = "Subject: " +subject+ '\n' +message

smtp_object.send(from_address, to_address, msg)

smtp_object.quit()