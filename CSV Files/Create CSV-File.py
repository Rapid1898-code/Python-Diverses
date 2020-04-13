# DevNami: https://www.youtube.com/watch?v=T8IJ59s8ZoE

import csv

with open("test.csv","w",newline="") as fp:
    a = csv.writer(fp,delimiter=",")
    data=[["Stock","Sales"],
          ["100","24"],
          ["120","33"],
          ["23","5"]]
    a.writerows(data)

