import smtplib, ssl
import time
import random

port = 465  # For SSL
receiver_email = ["businessinquiries@thecollective-la.com"]
blackListedEmails = ["genesis45678901234@gmail.com","tonyjhab@gmail.com", "humirasupplements2@gmail.com","usdasuppliersgov@gmail.com", "tonyjhab@gmail.com", "genesis45678901234@gmail.com", "humirasupplements2@gmail.com", "irshad.reza.husain@gmail.com", "ektang7@gmail.com", "uclabdb8@gmail.com", "rishi.rishi.mukherjee@gmail.com"]
FILE = "/Users/child/Desktop/001 - WMDs/forwardSpam/sentences.txt"
FILE1 = "/Users/child/Desktop/001 - WMDs/forwardSpam/subjects.txt"
EMAIL_FILE = "/Users/child/Desktop/001 - WMDs/forwardSpam/mail_addresses.txt"
# Send email here
password = '' #Change password depending on email
# Create a secure SSL context

def findAddress(email):
    index = email.find("@")
    if email[index+1:len(email)] == "gmail.com\n":
        return "smtp.gmail.com"
    elif email[index+1:len(email)] == "outlook.com\n":
        return "smtp-mail.outlook.com"

def creator(counter, subjects, sentences):
    val1 = random.randint(1,13)
    val2 = random.randint(1,32)
    message = "Subject: " + subjects[random.randint(0,len(subjects)-1)] + " (Date: "+str(val1)+"/"+str(val2)+"/20)"
    message = message + """\

Dear Johnson,

"""
    for i in range(0, 25):
        sent = sentences[random.randint(0, len(sentences)-1)]
        message = message + " " + sent
    return message
    
def spammer(message, sender_email, smtp_server):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()

counter = 1
print("Number of Emails: ")
n = int(input())
f = open(FILE, 'r')
sentences = f.readlines()
f.close()
k = open(FILE1, 'r')
subjects = k.readlines()
k.close()
z = open(EMAIL_FILE, 'r')
senderEmailList = z.readlines()
z.close()

while counter < n:
    if counter%30 == 0:
        time.sleep(10)
        counter += 1
        continue
    else:
        try:
            sender_email = senderEmailList[random.randint(0,len(senderEmailList)-1)]
            message = creator(counter, subjects, sentences)
            print(str(counter) + " - " + sender_email)
            serv = "smtp.gmail.com"
            spammer(message, sender_email, serv)
            counter += 1
        except Exception as e:
            print(str(e))
            counter += 1
        time.sleep(1.5)
print('Done with spamming')






