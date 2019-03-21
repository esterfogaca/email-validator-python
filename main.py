import re

def valid_email(email):
    if re.fullmatch(r"(^([A-z0-9\.\-_]+@[A-z0-9]+)\.([A-z]{1,3}(\.[A-z]{1,2})?))", email):
        return email


def filter_email(emails):
#
#   O return abaixo faz o mesmo que essas linhas comentadas
#
#    valid_emails = []
#    for email in emails:
#        x = valid_email(email)
#        if x:
#            valid_emails.append(x)
#    return valid_emails

    return [ valid_email(email) for email in emails if valid_email(email) ]
