"""
    import pandas as pd
    erg = pd.date_range(end = datetime.today(), periods = 100).to_pydatetime().tolist()
    for i in erg: print(i.date())
    print(erg)
"""

"""
    import datetime
    def date_range(start, end):
        r = (end + datetime.timedelta (days=1) - start).days
        return [start + datetime.timedelta (days=i) for i in range (r)]
    start = datetime.date (2007,1,1)
    end = datetime.date (2008,2,1)
    dateList = date_range (start, end)
    print(dateList)
"""

import pandas as pd
from datetime import date

# Erstellung einer Datums-Liste vom aktuellstem bis zum  ältesten Datum im Format jjjj-mm-dd
def date_list (datum_von, datum_bis):
    mydates2  = []
    mydates = pd.date_range(datum_bis, datum_von).tolist()
    for i in range(len(mydates)-1,-1,-1): mydates2.append(mydates[i].strftime('%d.%m.%y'))
    return(mydates2)

#mydates2 = []
#mydates = pd.date_range("2020-03-28", date.today()).tolist()
#for i in range(len(mydates)-1,-1,-1): mydates2.append(mydates[i].strftime('%d.%m.%y'))
#print(mydates2)

datelist = date_list(date.today(), "2020-04-09")
print(datelist)


