import requests
from bs4 import BeautifulSoup
import csv

def fetch_legislators(url, assembly):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #get table with all info
    table = soup.find('table')
    #get rows of table excluding the first one
    rows = table.find_all('tr')[1:]  
    #make a list to store each person data
    members = []

    for row in rows:
        cells = row.find_all('td')

        #get email
        email = row.find('a', class_='email')
        email = email['href'].replace('mailto:', '').strip() if email else 'N/A'

        #get name
        name = cells[1].text.strip()
        last_name, first_name = [n.strip() for n in name.split(',', 1)]

        #get party
        party = cells[2].text.strip()
        #get district
        district = cells[4].text.strip()
        #get phonenumber
        phone = cells[6].text.strip()

        members.append({
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'party': party,
            'district': district,
            'phone': phone,
            'state': "Tennessee",
            'assembly': assembly
        })

    return members

url_and_assembly = [
    ('https://wapp.capitol.tn.gov/apps/LegislatorInfo/directory.aspx?chamber=H', 'House'),
    ('https://wapp.capitol.tn.gov/apps/LegislatorInfo/directory.aspx?chamber=S', 'Senate')
]

all_members = []
for url, assembly in url_and_assembly:
    all_members.extend(fetch_legislators(url, assembly))

with open('Legislators.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['first_name', 'last_name', 'email', 'party', 'district', 'phone', 'state', 'assembly']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_members)

print("CSV file created successfully.")
