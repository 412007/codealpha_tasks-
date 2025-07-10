import re

input_file = 'input.txt'
output_file = 'emails.txt'

email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

with open(input_file, 'r') as file:
    content = file.read()
    emails = re.findall(email_pattern, content)

with open(output_file, 'w') as file:
    for email in emails:
        file.write(email + '\n')

print(f"Extracted {len(emails)} email(s) and saved to {output_file}")