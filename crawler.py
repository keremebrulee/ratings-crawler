import requests
import json
import csv

# Select where you want to save the ratings file 
write_csv = " "  

# Replace XX with your Mubi user id and YY with the total number of ratings you have
scrape_url = 'https://mubi.com/services/api/ratings?user_id=XX&page=1&per_page=YY'
response = requests.get(scrape_url)

if response.status_code == 200:
    soup = json.loads(response.text)

for i in soup:
    with open(write_csv, 'at',encoding = 'utf-8') as csv_obj:
        write = csv.writer(csv_obj) 
        directors_list = list()
        for j in i["film"]["directors"]:
            directors_list.append(j["name"])
        write.writerow([i["film"]["title"], i["film"]["year"], i["overall"], directors_list])
