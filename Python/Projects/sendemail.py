import smtplib


sender = "laibasmd@gmail.com"
reciever = "memonlaiba03@gmail.com"
password = "OVErlord,2001"
subject = "python email test"
body =  "i wrote an email"

#header
message = f"""From: Snopp Dog {sender}
To: Nikolas Cage {reciever}
Subject: {subject}
{body}"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()


server.login(sender,password)
print("Logged in...")

server.sendmail(sender,reciever,message)
print("Email has been sent")

#less secure apps no longer supported on google
#therefore this code is not complete
