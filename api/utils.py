import requests
from bs4 import BeautifulSoup
import json


def parse_duma():
    r = requests.get("http://duma.gov.ru/duma/factions/72100027/members/").text
    base_url = "http://duma.gov.ru"
    soup = BeautifulSoup(r, 'html.parser')
    dep_divs = soup.select('.person')

    dep_edr = {}
    for div in dep_divs:
        if div.a.picture:
            dep_edr[div.div.h2.a.span.strong.text + " " +
                    div.div.h2.a.span.span.text] = base_url + div.a.picture.img["src"]

    with open("sr.csv", 'w') as f:
        json.dump(dep_edr, f)


with open("edro.csv", "r") as f:
    dep_edr = json.load(f)


with open("kprf.csv", "r") as f:
    dep_kprf = json.load(f)


with open("ldpr.csv", "r") as f:
    dep_ldpr = json.load(f)


with open("sr.csv", "r") as f:
    dep_sr = json.load(f)


def is_from_edro(name):
    if(name in dep_edr):
        return True
    return False


def is_from_kprf(name):
    if(name in dep_kprf):
        return True
    return False


def is_from_ldpr(name):
    if(name in dep_ldpr):
        return True
    return False


def is_from_sr(name):
    if(name in dep_sr):
        return True
    return False
