import requests
import pprint as pp

def get_dec_by_name(name):
  name_url = "https://declarator.org/api/v1/search/person-sections/?name="

  res = requests.get(name_url + name).json()
  if res["count"] == 1:
    return res["results"][0]
  else:
    for person in res["results"]:
      if (name == person["name"]):
        return person
  return {}


def summarize_person(person):
  summ = {}

  summ["name"] = person["name"]
  summ["id"] = person["id"]
  summ["square"] = 0
  # iterate over positions
  for position in person["sections"]:

    # iterate over years
    for section in position["sections"]:
      year = section['main']['year']
      summ[year] = {}
      summ[year]["position"] = position['position']
      summ[year]["square"] = 0
      for real_estate in section["real_estates"]:
        '''
        if not real_estate["relative"]:
          print("his " + str(real_estate["square"]) + " mt of " + str(real_estate["type"]["name"]))
          
        else:
          print(real_estate["relative"]["name"] + "'s "  + str(real_estate["square"]) + " mt of " + str(real_estate["type"]["name"]))
        '''
        summ[year]["square"] += real_estate["square"]
        summ["square"] += real_estate["square"]
  return summ


def download_dump():
  url = "https://declarator.org/media/dumps/declarations.json"

  
person = get_dec_by_name("Струков Константин Иванович")
summ = summarize_person(person)
pp.pprint(summ)