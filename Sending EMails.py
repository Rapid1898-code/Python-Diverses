import smtplib
from email.mime.text import MIMEText

s = smtplib.SMTP('smtp.gmail.com', 587)
#s.set_debuglevel(1)
print(s.ehlo())
print(s.starttls())
print(s.login('markuspolzer73@gmail.com', 'rvknapzlbzttxbtw'))
msg = MIMEText("Das ist der Text des Mails")
sender = 'markuspolzer73@gmail.com'
recipients = ['markuspolzer73@gmail.com']
# recipients = ['rapid1898@gmail.com', 'markus.polzer@r-software.at', 'markuspolzer73@gmail.com']
msg['Subject'] = "Titel des Mails"
msg['From'] = sender
msg['To'] = ", ".join(recipients)
s.sendmail(sender, recipients, msg.as_string())
s.quit()





