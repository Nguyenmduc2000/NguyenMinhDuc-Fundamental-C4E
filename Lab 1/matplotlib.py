import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('ducnguyen1312000@gmail.com','simbat2010')
message = 'Nono'
server.sendmail('ducnguyen1312000@gmail.com','ducnguyen1312000@gmail.com',message)
server.quit()