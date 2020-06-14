from datetime import datetime
now = datetime.now()
d = datetime(2020,3,5,19,27,23)
print(now)
print(d)
diff = now-d
print(diff.days)
print(diff.seconds)
print(diff.total_seconds()/60)

