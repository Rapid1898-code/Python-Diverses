#output = [['/apple-aktie', '17.04.20', '16.04.20', '15.04.20', '14.04.20', '09.04.20', '08.04.20', '07.04.20', '06.04.20', '03.04.20', '02.04.20', '01.04.20'],
#         ['/apple-aktie', '257,95', '264,70', '259,95', '259,80', '243,25', '244,10', '244,00', '234,55', '224,75', '222,90', '225,20']]

#with open ('test.txt', 'a') as file:
#    file.write ("%s\n" % output[0])
#    file.write ("%s\n" % output[1])


import json
output = []
try:
    with open("test.txt") as f:
        for line in f:
            line = line.replace("'",'"')
            output.append(json.loads(line.strip()))
        print(output)
except:
    pass


