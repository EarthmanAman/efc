import imaplib

M = imaplib.IMAP4_SSL("imap.hashimathman.com")
email = "contact@hashimathman.com"
password = "rQ6X-8w$F1p%qtC"

M.login(email, password)