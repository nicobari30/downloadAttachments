from imap_tools import MailBox
import re
import datetime
import os
from getpass import getpass

imap=input("Insert imap server:")
directory=input("Insert path of attachments directory:")
username=input("Insert username:")
passwd = getpass(prompt="Insert password:")

with MailBox(imap).login(username, passwd) as mailbox:
    for msg in mailbox.fetch():
        for att in msg.attachments:
            print(att.filename, att.content_type)
            if(att.filename != '' ):
                name=att.filename
                name=name.replace(' ','')
                name=name.replace('\r','')
                name=name.replace('\n','')
                name=name.replace('\t','')
                name=name.replace('\b','')
                print(name)
                year=msg.date.year
                if not(os.path.exists(directory+"\\"+str(year))):
                    os.makedirs(directory+"\\"+str(year))
                month=msg.date.month
                if not(os.path.exists(directory+"\\"+str(year)+"\\"+str(month)+"-"+str(year))):
                    os.makedirs(directory+"\\"+str(year)+"\\"+str(month)+"-"+str(year))
                day=msg.date.day
                if not(os.path.exists(directory+"\\"+str(year)+"\\"+str(month)+"-"+str(year)+"\\"+str(month)+"-"+str(day)+"-"+str(year))):
                    os.makedirs(directory+"\\"+str(year)+"\\"+str(month)+"-"+str(year)+"\\"+str(month)+"-"+str(day)+"-"+str(year))
                if not(os.path.exists(directory+"\\"+str(year)+"\\"+str(month)+"-"+str(year)+"\\"+str(month)+"-"+str(day)+"-"+str(year)+"\\{}".format(name))):
                    with open(directory+"\\"+str(year)+"\\"+str(month)+"-"+str(year)+"\\"+str(month)+"-"+str(day)+"-"+str(year)+"\\{}".format(name), 'wb') as f:
                        f.write(att.payload)
print("END")
