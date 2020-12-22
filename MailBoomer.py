import smtplib


def send_mail():
    #your mail
    send = input("[+] Enter Your Email >>> ")

    #your password
    password = input("[+] Enter Your Password >>> ")

    #Send to:
    to = input("[+] Send to >>> ")

    #message
    message = input("[+] Enter Message >>> ")

    #how many time send
    how_many = int(input("[+] How Many Times? >>> "))
    print("Starting....")
    for i in range(how_many):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(send, password)
        server.sendmail(send, to, message)
        print("[+] Mail Sent!")
send_mail()