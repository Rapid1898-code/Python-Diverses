# https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup

URL = "https://www.monster.at/jobs/suche/?q=Software-Devel&where=Graz"  # Ergebnisseite mit Suche nach Software-Devel und Graz
page = requests.get(URL)    # Internetseite in Python speichern
soup = BeautifulSoup(page.content, "html.parser")   # Internetseite mit BeautifulSoup einlesen und parsen
results = soup.find(id="SearchResults")     # HTML-mit den Suchresultaten wird eingelsen - Abfrage auf ID - daher eindeutig
# print(results.prettify())

job_elems = results.find_all("section", class_="card-content")
            #Einzelne Elemente des Suchergebnisses links werden eingelesen
            #und in einem Array gespeichert
for job_elem in job_elems:
        #f�r jedes einzelne Job-Suchergebnis wird der Teil f�r Titel / Company / Location gespeichert
    title_elem = job_elem.find("h2", class_="title")
    company_elem = job_elem.find("div", class_="company")
    location_elem = job_elem.find("div", class_="location")
    if None in (title_elem, company_elem, location_elem):   # Wenn Absturz wg. leerem Element - z.B. wg. Foto ohne Text
                                                            # erfolgt keine Weiterverarbeitung
        continue
    print(title_elem.text.strip())      # Textteil wird herauskopiert f�r den jeweiligen Bereich
    print(company_elem.text.strip())    # f�r Titel / Company / Location
    print(location_elem.text.strip(), "\n")

python_jobs = results.find_all("h2", string=lambda text: "area" in text.lower())
    # hier ein  Beispiel wenn nur bestimmte Jobs mit einem bestimmten Text ausgegeben werden sollen







