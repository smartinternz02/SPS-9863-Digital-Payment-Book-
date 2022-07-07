import smtplib
import os
s = smtplib.SMTP('smtp.gmail.com', 587)
def sendmail(TEXT,email,SUBJECT):
    #print("sorry we cant process your candidature")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login("memail", "madhav@1234")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("mdhvsnair@gmail.com", email, message)
    s.quit()


