s="76.4B"
if "B" in s:
    decimal_place = s.find(".")
    b_place = s.find("B")
    s = s.replace(".","").replace("B","")
    for i in range(9 - (b_place - decimal_place -1)): s = s + "0"

print(decimal_place)
print(b_place)
print(s)