#!/usr/bin/python
import random
import fileinput
import smtplib
from email.mime.text import MIMEText

smtp_host = "localhost"
santa_email = "santaselves@mototesta.com"
email_body_file = "santasmessage.txt"
email_body_fp = open(email_body_file, 'rb')
email_body_text = email_body_fp.read()
email_body_fp.close()

def readnames():
    names = []
    for line in fileinput.input():
        line = line.strip()
        names.append( line.rsplit(',') )
    return names

def sendmail(giver, recip):
    msg = MIMEText("Season's Greetings!\n\nYou've been magically chosen to be the Secret Santa for " + recip[0] + ".\n\n" + email_body_text)
    msg['Subject'] = "2012 Secret Santa Drawing"
    msg['From'] = santa_email
    msg['To'] = giver[1]
    email = smtplib.SMTP(smtp_host)
    email.sendmail(santa_email, [giver[1]], msg.as_string())
    print santa_email + "\n" + giver[1] + "\n" + msg.as_string()

def getpair(fromlist, topairs):
    if len(fromlist) > 1:
        giver = fromlist.pop()
        recip = getpair(fromlist, topairs)
        topairs.append( (giver, recip) )
        return giver
    else :
        return fromlist[0]

names = readnames()
random.shuffle(names)
pairs = []
# magic happens here:
pairs.append( (names[0], getpair(names, pairs)) )
print pairs
for fromto in pairs:
    print "----"
    sendmail(fromto[0], fromto[1])
    print "^^^^"
