import re

with open('text.txt', 'r') as file:
    text = file.read()
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    phone_numbers = re.findall(phone_pattern, text)
    email_addresses = re.findall(email_pattern, text)

with open('Phone numbers + Email addresses.txt', 'w') as file:
    file.write('Phone numbers:\n')
    for phone_number in phone_numbers:
        file.write(phone_number + '\n')
    file.write('\nEmail addresses:\n')
    for email_address in email_addresses:
        file.write(email_address + '\n')

print('phone numbers: ', phone_numbers)
print('email addresses: ', email_addresses)
#print(text)
