import requests
from bs4 import BeautifulSoup
import codecs
import re

eastchester = requests.get("https://www.eufsdk12.org/domain/76")
soup = BeautifulSoup(eastchester.text, "html.parser")
email_elements = soup.findAll("li", class_="staffemail")
decoded_emails = []

for element in email_elements:
    script = element.find("script").string if element.find("script") else None
    if script:
        matches =  re.findall(r"swrot13\('([^']+)'\)", script)
        if matches:
            encoded_email = matches[0]
            decoded_email = codecs.decode(encoded_email, 'rot_13')
            decoded_emails.append(decoded_email)
for email in decoded_emails:
    print(email)