import json
import pprint as pp
import pandas as pd
import tqdm


def nohome1(person):
    summ = {}
    summ["name"] = person["name"]
    summ["id"] = person["id"]

    for section in person["sections"]:
        year = section['main']['year']
        summ["year"] = year 
        flag = 0
        for real_estate in section["real_estates"]:
            if real_estate['type']['id'] == 4 or real_estate['type']['id'] == 3 or real_estate['type']['id'] == 6 :
                flag = 1
        if section['incomes'] != [] and flag == 0:
            if  section['incomes'][0]['size'] > 10000000:
                #summ[year]['type'] = "без определенного места жительства"
                summ["income"] = section['incomes'][0]['size']
                return summ

    return 0
 

with open("persons_parsed.json", 'r') as f:
    persons = json.load(f)

rez=[]
for key in tqdm.tqdm(persons):
    person = persons[key]
    summ = nohome1(person)
    if summ != 0:
        rez.append(summ)
        #pp.pprint(summ)
df = pd.DataFrame(rez)
df=df.sort_values('income',ascending=False)
print(df.head(10))
