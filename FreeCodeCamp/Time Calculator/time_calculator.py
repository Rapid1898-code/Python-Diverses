def add_time(start, duration, day=False):
    weekdays = {"MONDAY":1,"TUESDAY":2,"WEDNESDAY":3,"THURSDAY":4,"FRIDAY":5,
                "SATURDAY":6,"SUNDAY":7}
    if day != False:
        day = day.upper()
        start_weekday = weekdays[day]
    am_pm = start[-3:].strip()
    start_hour = start[:-3].split(":")[0]
    start_min = start[:-3].split(":")[1]
    dur_hour = duration.split(":")[0]
    dur_min = duration.split (":")[1]

    days = int(dur_hour) // 24
    hour_rest = int(dur_hour) % 24

    if am_pm == "PM": start_hour = int(start_hour) + 12

    hour = int(start_hour) + int(hour_rest)
    min = int(start_min) + int(dur_min)
    if min >= 60:
        hour += 1
        min -= 60
    if hour >= 24:
        hour -= 24
        days += 1
    if hour > 12:
        hour -= 12
        am_pm = "PM"
    elif hour == 12: am_pm = "PM"
    else: am_pm = "AM"
    if hour == 0: hour = 12
    if len(str(min)) == 1: min = "0" + str(min)

    erg = str(hour) + ":" + str(min) + " " + am_pm
    if day != False:
        tmp_weekday = start_weekday  + days%7
        if tmp_weekday > 7: tmp_weekday -= 7
        key = list (weekdays.keys ())[list (weekdays.values ()).index (tmp_weekday)]
        erg = erg + ", " + key.capitalize()

    if days == 1: erg = erg + " (next day)"
    elif days > 1: erg = erg + " (" + str(days) + " days later)"

    return erg

#print(add_time("11:06 PM", "2:02"))
#print("<" + add_time("8:16 PM", "466:02") + ">")
#print(add_time("8:16 PM", "466:02", "tuesday"))
