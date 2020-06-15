Pay Attention:
- before you execute the program, close both excelsheets Dashboard.xlsx and AlertTracker.xlsx (otherwise there are possible conflicts when opening the xlsx in the program)
- when you want to delete a stock from the AlertTracker.xlsx only the the symbol in the column A (no deleting of the whole line with Ctrl-"-" foir example - could cause problems in sorting and updating)

Parameters in Dashboard.xlsx
C3
if you enter a stock symboil it will be added to the AlertTracker.xlsx - after the entry go to the next line with <Enter>
when the symbol is allready in the xlsx => no action

A15
Mail-adress where the manual alerts from the dashborad or the alerts from stocktwits are sent to

D15
App-password from your googlemailaccount (for securtiy reason can´t use your normal googlemail-pw
you have to use instead a special generated one - instructions for generation you can find here: https://support.google.com/mail/answer/185833?hl=en

A19
how long back on stocktwits should be checked for alerts
with input 0 there is no scroll down - and so only the latest twits are checked
when there is a entry - eg. 4 - then there will be 4 page down scrolls for searching
if you want only the latest updates - so make 0 as entry
when the alerted symbol is allready in the xlsx => no action

A22
update interval for the AlertTracker.xlsx in seconds

D22
update interval for the Stocktwits-lookup in minutes

