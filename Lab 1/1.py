import smtplib
import datetime
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('ducnguyen1312000@gmail.com','simbat2010')
message = 'Em đau đẻ'

server.quit()
while True: 
    time= datetime.datetime.now().strftime("%I:%M %p")
    if time == "07:00 AM":
        server.sendmail('ducnguyen1312000@gmail.com','ducnguyen1312000@gmail.com',message)
        server.quit()
