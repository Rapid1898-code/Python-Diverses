from datetime import datetime, timedelta
s = "9/29/2019"
dt = datetime.strptime(s, "%d/%m/%Y")

#"%#d/%m/%Y"
#ValueError: '#' is a bad directive in format '%#d/%m/%Y'

#"%-d/%m/%Y"
#ValueError: '-' is a bad directive in format '%-d/%m/%Y'

#"%d/%m/%Y"
#ValueError: time data "'9/29/2019'" does not match format '%d/%m/%Y'
