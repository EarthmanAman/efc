import imaplib
import email
import csv
from f import FetchEmail

mail = imaplib.IMAP4_SSL("imap.gmail.com")
email1 = "hashimathman.info@gmail.com"
password = "ppeyxjjouqgplfmw"

mail.login(email1, password)
mail.select("Inbox")

count = ''
try:
    return_code, data = mail.search(None, 'UnSeen')
    #count = len(mail_ids[0].split(" "))
    mail_ids = data[0].decode()
    id_list = mail_ids.split()[-4:]
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])
    with open('persons.csv', 'w', newline="") as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['From', 'Subject'])
        for i in range(latest_email_id,first_email_id, -1):
    
            typ, data = mail.fetch(str(i),'(RFC822)')
            for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1].decode("utf-8"))
                        email_subject = msg['subject']
                        email_from = msg['from']
                        print(email_subject)
                        filewriter.writerow([email_from, email_subject])
        mail.close()
except Exception as e: print(e)

print (count)

# em = FetchEmail("imap.gmail.com", email1, password)
# emls = em.fetch_unread_messages()

# m = em.save_attachment(emls[1], "./result")

# print(m)