import smtplib
smtpObject = smtplib.SMTP('smtp.gmail.com', 587)

print(smtpObject.ehlo())
smtpObject.starttls()
print(smtpObject.login('test@gmail.com', 'test!'))
