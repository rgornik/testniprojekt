import requests
from BeautifulSoup import BeautifulSoup
import csv

url = "https://scrapebook22.appspot.com/"

r = requests.get(url)
#print r.text

#print r

soup = BeautifulSoup(r.text)

#print soup.head.title.string

all_emails = []
for link in soup.findAll("a"):
    if "person" in link["href"]:
        #print link
        detail_r = requests.get(url + link["href"])
        #print detail_r.text

        detail_soup = BeautifulSoup(detail_r.text)

        email = detail_soup.find("span", attrs={"class": "email"})
        name = None
        for naslov in detail_soup.findAll("h1"):
            if "Hello, ninja!" not in naslov.string:
                name = naslov.string
        print email.string
        all_emails.append([name, email.string])

print all_emails

with open("output.csv", "wb") as out_csv:
    writer = csv.writer(out_csv, delimiter=";")
    for line in all_emails:
        print line
        writer.writerow(line)