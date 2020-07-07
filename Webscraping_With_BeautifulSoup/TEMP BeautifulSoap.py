import requests
from bs4 import BeautifulSoup

link1 = "https://tradingeconomics.com/italy/stock-market"
page = requests.get (link1)
soup = BeautifulSoup (page.content, "html.parser")

soup  = soup.find("table", attrs={"class": "table table-hover sortable-theme-minimal table-heatmap"})
#print(div.prettify())


tmp = []
erg = []

for e in soup.find_all("td"):
    tmp.append(e.text.strip())

for i in range(0,len(tmp),8):
    erg.append((tmp[i]+".MI",tmp[i+1]))

erg.sort()
print(erg)
print(len(erg))

indizes["mib"] = ['TEN.MI', 'TIT.MI', 'TRN.MI', 'UBI.MI', 'UNI.MI']
print(len(l))

[('A2A.MI', 'A2A'), ('ATL.MI', 'Atlantia'), ('AZM.MI', 'Azimut Holding'), ('BAMI.MI', 'Banco BPM'), ('BGN.MI', 'Banca Generali'), ('BMED.MI', 'Banca Mediolanum'), ('BZU.MI', 'Buzzi Unicem'), ('CNHI.MI', 'CNH Industrial'), ('CPR.MI', 'Davide Campari'), ('DIA.MI', 'DiaSorin SpA'), ('ENEL.MI', 'Enel'), ('ENI.MI', 'Eni Group'), ('EXO.MI', 'Exor'), ('FBK.MI', 'Finecobank'), ('FCA.MI', 'Fiat Chrysler'), ('G.MI', 'Assicurazioni Generali'), ('IG.MI', 'Italgas SpA'), ('IP.MI', 'Interpump Group'), ('ISP.MI', 'Intesa Sanpaolo'), ('LDO.MI', 'Leonardo SpA'), ('MB.MI', 'Mediobanca'), ('MONC.MI', 'Moncler'), ('MS.MI', 'Mediaset'), ('PCP.MI', 'Pirelli & C'), ('PIRC.MI', 'Pirelli'), ('PRY.MI', 'Prysmian'), ('PST.MI', 'Poste Italiane'), ('RACE.MI', 'Ferrari'), ('REC.MI', 'Recordati'), ('SFER.MI', 'Salvatore Ferragamo'), ('SPM.MI', 'Saipem'), ('SRG.MI', 'Snam'), ('STM.MI', 'STMicroelectronics'), ('TIT.MI', 'Telecom Italia'), ('TRN.MI', 'Terna Rete Elettrica Nazionale'), ('TS.MI', 'Tenaris S.a.'), ('UBI.MI', 'UBI Banca'), ('UCG.MI', 'UniCredit'), ('UNI.MI', 'Unipol Gruppo'), ('US.MI', 'UnipolSai Assicurazioni')]


