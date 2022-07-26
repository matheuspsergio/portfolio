'''
#Basic ideia of the script

Open the website as a json
iter thorugh all IDs
for each ID, open the corresponding json
grab all the data and append to a csv
after the last id, change the counter for the start page
repeat
if the request don't generate new ids (returns empty page instead), break the loop, and finish
'''


#libraries
from requests_html import HTMLSession
import json
import csv


#variable that sotres the page in the website to scrape (r variable)
count = 0
#a loop to run while there are new pages eith content
while True:
    #starting a html session and loading the content as json
    session = HTMLSession()
    r = session.get('https://desaparecidos-api.pcivil.rj.gov.br/missings', params={'pageSize': 100, 'pageStart': count})
    missing = json.loads(r.text)
    #cheking if the page is empty. if it is (no more people), break the loop
    if len(missing['content']) == 0:
        break
    #iterating through each person in the page got above
    for person in missing['content']:
        #there's a separete html for each person that can be accessed with the id that we're getting below
        id = person['id']
        #going to the html specific to heach person
        info = 'https://desaparecidos-api.pcivil.rj.gov.br/missings/'+ str(id)
        t = session.get(info)
        carac = json.loads(t.text)
        #creating variables to store each info according to its respective class
        id = carac['name']
        age = carac['age']
        placeOfDisappearance = carac['placeOfDisappearance']
        dateOfDisappearance = carac['dateOfDisappearance']
        isFound = carac['isFound']
        isDead = carac['isDead']
        isActive = carac['isActive']
        obs = carac['obs']
        #concatenating those variables of a given person in a list to be appended as row in the csv
        row = [id, age, placeOfDisappearance, isFound, isDead, isActive, obs]
        #adding the data to an external file
        with open('teste.csv', 'a', encoding = 'UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(row)
    count += 1

    
'''' All the keys from missing people
id
name
age
placeOfDisappearance
dateOfDisappearance
isFound
isDead
isActive
mother
father
eyeColor
hairColor
skinColor
scar
tattoo
clothing
obs
photo
isSocialPic
createdBy
createdAt
updatedBy
updatedAt
idSCO
'''