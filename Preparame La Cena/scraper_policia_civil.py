from requests_html import HTMLSession
import json
import csv

#starting a html session

count = 0
while True:
    session = HTMLSession()
    r = session.get('https://desaparecidos-api.pcivil.rj.gov.br/missings', params={'pageSize': 100, 'pageStart': count})
    missing = json.loads(r.text)
    if len(missing['content']) < 15:
        break
    for person in missing['content']:
        id = person['id']
        #aqui pode virar um função pra deixar o código mais limpo
        info = 'https://desaparecidos-api.pcivil.rj.gov.br/missings/'+ str(id)
        t = session.get(info)
        carac = json.loads(t.text)
        id = carac['name']
        age = carac['age']
        placeOfDisappearance = carac['placeOfDisappearance']
        dateOfDisappearance = carac['dateOfDisappearance']
        isFound = carac['isFound']
        isDead = carac['isDead']
        isActive = carac['isActive']
        row = [id, age, placeOfDisappearance, isFound, isDead, isActive]
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


#How the bagulho vai funcionar

#Open the website as a json
#iter thorugh all IDs
#for each ID, open the corresponding json
#grab all the data
#after the last id, change the counter for the start page
#repeat
#if the requests doesn't generate new ids, break the loop, and finish