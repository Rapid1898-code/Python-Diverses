from datetime import datetime, timedelta
from datetime import date
import calendar

l1 = [('2020-05-29', 317.940002), ('2020-04-30', 293.799988), ('2020-03-31', 254.289993), ('2020-02-28', 273.359985)]
l2 = [('2020-05-29', 3044.310059), ('2020-04-30', 2912.429932), ('2020-03-31', 2584.590088), ('2020-02-28', 2954.219971)]
l1_change = []
l2_change = []

for i in range(3,0,-1):
    l1_change.append(round(((l1[i][1] - l1[i-1][1]) / l1[i-1][1])*100,2))
    l2_change.append(round(((l2[i][1] - l2[i-1][1]) / l2[i-1][1])*100,2))

print(l1_change)
print(l2_change)










