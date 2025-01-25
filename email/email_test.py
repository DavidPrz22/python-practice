import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Path("index.html").read_text()
html_template = Template(html)
html_template.substitute({"receiver":"Lewandosky", "sender":"Laporta", "email":"laliga@gmail.com"})




# email = EmailMessage()

# email["from"] = "Didier Henry"
# email["to"] = "deivid.prz3412@gmail.com"
# email["subject"] = "You won 10000000 dollar!"

# email.set_content("STOP WASTING TIME BRO!")

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as  smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('davoalbert79@gmail.com', 'David*3412')
#     smtp.send_message(email)