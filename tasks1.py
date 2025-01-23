#task 1

with open("email.txt", "r") as file:
    email_list = file.readlines()

domains = set()

for email in email_list:
    e_mail = email.split(".")
    domains.add("." + e_mail[-1].strip())
for domain in domains:
    print(domain)
