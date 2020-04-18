import requests
from bs4 import BeautifulSoup

def dax_stocks ():
    page = requests.get ("https://www.ariva.de/dax-30")
    soup = BeautifulSoup (page.content, "html.parser")
    table  = soup.find(id="result_table_0")
    dax = {}
    for row  in table.find_all("td"):
        if row.get("class") == ["ellipsis", "nobr", "new", "padding-right-5"]:
            dax[row.find("a")["href"]] = row.text.strip()
            #print(row.find("a")["href"])
            #print(row.get("class"))
            #print(row)
    print(dax)

#dax_stocks()


dict2 = {'/infineon-aktie': ' Infineon ', '/volkswagen_vz-aktie': ' Volkswagen Vz ', '/continental-aktie': ' Continental ', '/bmw-aktie': ' BMW St ', '/heidelbergcement-aktie': ' HeidelbergCement ', '/mtu_aero_engines-aktie': ' MTU Aero Engines ', '/covestro-aktie': ' Covestro ', '/siemens-aktie': ' Siemens ', '/daimler-aktie': ' Daimler ', '/munich_re-aktie': ' Munich Re ', '/basf-aktie': ' BASF ', '/deutsche_bank-aktie': ' Dt. Bank ', '/deutsche_post-aktie': ' Dt. Post ', '/adidas-aktie': ' adidas ', '/allianz-aktie': ' Allianz ', '/sap-aktie': ' SAP ', '/deutsche_telekom-aktie': ' Dt. Telekom ', '/linde_plc-aktie': ' Linde PLC ', '/bayer-aktie': ' Bayer ', '/henkel_vz-aktie': ' Henkel Vz ', '/lufthansa-aktie': ' Lufthansa ', '/beiersdorf-aktie': ' Beiersdorf ', '/merck_kgaa-aktie': ' Merck KGaA ', '/fresenius_medical_care-aktie': ' Fresenius Medical Care ', '/deutsche_b%C3%B6rse-aktie': ' Dt. Börse ', '/fresenius-aktie': ' Fresenius ', '/wirecard-aktie': ' Wirecard ', '/rwe-aktie': ' RWE St ', '/e-on-aktie': ' E.ON ', '/vonovia-aktie': ' Vonovia '}
for stock_key, stock_name in dict2.items():
    print ("Key: ",stock_key," Name: ", stock_name)


