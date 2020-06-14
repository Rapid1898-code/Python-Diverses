import requests
from bs4 import BeautifulSoup
import smtplib
import xlwings as xw
from email.mime.text import MIMEText
from datetime import datetime
import time
import timeit
import sys
import os

# Sortierung excel sheet with xlwings
def xl_col_sort(sheet,col_num):
    sheet.range((2,col_num)).api.Sort(Key1=sheet.range((2,col_num)).api, Order1=1)
    return

# Countdown in einer Zeile
def wait_countdown (sek):
    for i in range (sek, 0, -1):
        sys.stdout.write (str (i) + ' ')
        sys.stdout.flush ()
        time.sleep (1)
    print("\n")

def send_mail(msg_txt):
    s = smtplib.SMTP ('smtp.gmail.com', 587)  # SMTP-Server and port number from the mail provider (e.g. GMail)
    print (s.ehlo ())  # Check if OK - Response 250 means connection is ok
    print (s.starttls ())  # Check if OK
    print (s.login (ws_db["A15"].value, ws_db["D15"].value))  # Check if OK
    msg = MIMEText (msg_txt)
    sender = 'markuspolzer73@gmail.com'
    recipients = ['rapid1898@gmail.com']
    msg['Subject'] = "New Stock for AlertTracker: " + symbol + "-" + name
    msg['From'] = sender
    msg['To'] = ", ".join (recipients)
    s.sendmail (sender, recipients, msg.as_string ())
    s.quit ()

db = "Dashboard.xlsx"
at = "AlertTracker.xlsx"
path = os.getcwd()
fn = path + "\\" + at
print(fn)

wb = xw.Book (db)
wb2 = xw.Book (at)
# ws_at = wb2.sheets["AlertTracker"]
# ws_at["A1"].value = "###"
# xl_col_sort(ws_at,1)
# ws_at["A1"].value = "Symbol"

while True:
    try:
        start_updatestocks = timeit.default_timer ()
        ws_db = wb.sheets["Dashboard"]
        ws_at = wb2.sheets["AlertTracker"]
        # Sort AlertTracker with headline as top
        ws_at["A1"].value = "###"
        xl_col_sort (ws_at, 1)
        ws_at["A1"].value = "Symbol"
        stocks = ws_at.range ('A2:A100').value
        sek = int(ws_db["A22"].value)
        # Wait for X seconds with countdown
        print("AlertTracker update every ",sek,"sec...")
        wait_countdown(sek)

        if ws_db["C3"].value != None and ws_db["C3"].value not in stocks:
            msg = ""
            symbol = ws_db["C3"].value
            link = "https://finance.yahoo.com/quote/" + symbol
            link2 = link + "/profile?p=" + symbol
            page = requests.get (link)
            soup = BeautifulSoup (page.content, "html.parser")

            # Read Volumes
            table = soup.find ('div', id="quote-header")
            volume = soup.find ('td', attrs={"data-test": "TD_VOLUME-value"}).text.strip ()
            avg_volume = soup.find ('td', attrs={"data-test": "AVERAGE_VOLUME_3MONTH-value"}).text.strip ()

            # Read Ranges
            d_r_tmp = soup.find ('td', attrs={"data-test": "DAYS_RANGE-value"}).text.strip ().split ('-')
            day_range_from, day_range_to = d_r_tmp[0].strip (), d_r_tmp[1].strip ()
            f_r_temp = soup.find ('td', attrs={"data-test": "FIFTY_TWO_WK_RANGE-value"}).text.strip ().split ('-')
            fifty_range_from, fifty_range_to = f_r_temp[0].strip (), f_r_temp[1].strip ()

            # Read stockname, actual price, daychange
            table = soup.find ('div', id="quote-header-info")
            name = table.find ("h1").text.split ("-")[1].strip ()
            price = soup.find ('span', attrs={"data-reactid": "14"}).text.strip ()
            daychange_tmp = soup.find ('span', attrs={"data-reactid": "16"}).text.strip ().split ("(")
            daychange = daychange_tmp[0].strip ()
            daychange_perc = daychange_tmp[1].strip ().replace (")", "")

            # Read MarketCap, PrevClose, PE, EPS
            marketcap = soup.find ('td', attrs={"data-test": "MARKET_CAP-value"}).text.strip ()
            prevclose = soup.find ('td', attrs={"data-test": "PREV_CLOSE-value"}).text.strip ()
            pe_ratio = soup.find ('td', attrs={"data-test": "PE_RATIO-value"}).text.strip ()
            eps_ratio = soup.find ('td', attrs={"data-test": "EPS_RATIO-value"}).text.strip ()

            # Read Additional Infos
            page = requests.get (link2)
            soup = BeautifulSoup (page.content, "html.parser")
            empl = soup.find ('span', attrs={"data-reactid": "30"})
            # there 2 different kinds of site-information - so there are 2 ways
            if empl != None:
                empl = empl.text.strip()
                sector_tmp = soup.find_all ('span', attrs={"data-reactid": "21"})
                for row in sector_tmp:
                    if row.get ("class") != None: sector = row.text.strip ()
                industry_tmp = soup.find_all ('span', attrs={"data-reactid": "25"})
                for row in industry_tmp:
                    if row.get ("class") != None: industry = row.text.strip ()
                description = soup.find ('p', attrs={"data-reactid": "141"}).text.strip ()
            else:
                table = soup.find ('div', attrs={"class": "asset-profile-container"})
                spans = table.find_all ("span")
                sector = spans[1].text.strip()
                industry = spans[3].text.strip()
                empl = spans[5].text.strip()
                table = soup.find ('section', attrs={"class": "quote-sub-section Mt(30px)"})
                description = table.find("p").text.strip()

            # Send Mail
            msg_txt ="DASHBOARD\n" \
                     "\nCurrent Volume: " + volume + \
                     "\nAverage Volume: "+ avg_volume + \
                     "\nDay Low/High: "+ day_range_from + " / " + day_range_to + \
                     "\n52W Range: " + fifty_range_from + " / " + fifty_range_to + "\n" + \
                     "\nSymbol-Name: " + symbol + " - " + name + \
                     "\nSector :" + sector + \
                     "\nIndustry: " + industry + \
                     "\nCurrent Price (day change %): " + price + " " + daychange_perc + "\n" + \
                     "\nMarketCap: " + marketcap + \
                     "\nPrev close: " + prevclose + \
                     "\n# of Employees: " + empl + "\n" + \
                     "\nCompany Description:\n" + description
            send_mail(msg_txt)

            for idx,cont in enumerate(stocks):
                if cont == None: break
            idx = str(idx+2)
            ws_at["A" + idx].value = symbol
            ws_at["B" + idx].value = name
            ws_at["C" + idx].value = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ws_at["D" + idx].value = sector
            ws_at["E" + idx].value = price
            ws_at["F" + idx].value = price
            ws_at["G" + idx].value = 0
            ws_at["H" + idx].value = 0
            ws_at["I" + idx].value = marketcap
            ws_at["J" + idx].value = pe_ratio
            ws_at["K" + idx].value = eps_ratio
            ws_at["L" + idx].value = fifty_range_from
            ws_at["M" + idx].value = fifty_range_to
            ws_at["N" + idx].value = 0
            ws_at["O" + idx].value = 0
        else:
            for i,cont in enumerate(stocks):
                idx = str(i + 2)
                if ws_at["A"+idx].value == None: break
                print("Update",cont,"in row", idx)
                link = "https://finance.yahoo.com/quote/" + cont
                page = requests.get (link)
                soup = BeautifulSoup (page.content, "html.parser")
                ws_at["C" + idx].value = datetime.now ().strftime ("%Y-%m-%d %H:%M:%S")
                table = soup.find ('div', id="quote-header-info")
                price = soup.find ('span', attrs={"data-reactid": "14"}).text.strip ()
                marketcap = soup.find ('td', attrs={"data-test": "MARKET_CAP-value"}).text.strip ()
                pe_ratio = soup.find ('td', attrs={"data-test": "PE_RATIO-value"}).text.strip ()
                eps_ratio = soup.find ('td', attrs={"data-test": "EPS_RATIO-value"}).text.strip ()
                d_r_tmp = soup.find ('td', attrs={"data-test": "DAYS_RANGE-value"}).text.strip ().split ('-')
                day_range_from, day_range_to = d_r_tmp[0].strip (), d_r_tmp[1].strip ()
                f_r_temp = soup.find ('td', attrs={"data-test": "FIFTY_TWO_WK_RANGE-value"}).text.strip ().split ('-')
                fifty_range_from, fifty_range_to = f_r_temp[0].strip (), f_r_temp[1].strip ()
                daychange_tmp = soup.find ('span', attrs={"data-reactid": "16"}).text.strip ().split ("(")
                daychange_perc = float(daychange_tmp[1].strip ().replace (")","").replace("+","").replace("-","").replace("%",""))
                ws_at["E" + idx].value = price
                ws_at["G" + idx].value = ws_at["E" + idx].value - ws_at["F" + idx].value
                ws_at["H" + idx].value = round((ws_at["E" + idx].value - ws_at["F" + idx].value) / ws_at["F" + idx].value * 100,2)
                ws_at["I" + idx].value = marketcap
                ws_at["J" + idx].value = pe_ratio
                ws_at["K" + idx].value = eps_ratio
                ws_at["L" + idx].value = fifty_range_from
                ws_at["M" + idx].value = fifty_range_to
                if ws_at["H" + idx].value < ws_at["N" + idx].value: ws_at["N" + idx].value = ws_at["H" + idx].value
                if ws_at["H" + idx].value > ws_at["O" + idx].value: ws_at["O" + idx].value = ws_at["H" + idx].value
            stop_updatestocks = timeit.default_timer ()
            print ("Total Time Stock Update: ", round ((stop_updatestocks - start_updatestocks), 0), "sek for", int(idx)-1, "stocks")
            print ("Avg. Time per Stock: ", round((stop_updatestocks - start_updatestocks) / (int(idx)-1), 2), "sek")
        wb2.save(fn)
        print("Saved to disk...")
    except Exception as e:
        print ("Error", e, "waiting for 30 sek...")
        wait_countdown (30)


