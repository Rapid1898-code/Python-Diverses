import subprocess, re, random, datetime
from random import randrange

# nord_output = subprocess.Popen(["C:/Program Files (x86)/NordVPN/NordVPN.exe", "status"], stdout=subprocess.PIPE)
#subprocess.call(["C:/Program Files (x86)/NordVPN/NordVPN.exe", "-c -g Belgium"])
#subprocess.call(["C:/Program Files (x86)/NordVPN/NordVPN.exe", "-c"])
#subprocess.call(["C:/Program Files (x86)/NordVPN/NordVPN.exe", "-d"])
#subprocess.call(["C:/Program Files (x86)/NordVPN/NordVPN.exe", "-c", "-g Austria"])
countries = ["Albania", "Argentina", "Australia", "Austria", "Belgium", "Canada", "Germany", "Israel", "Italy", "Norway",
             "Poland", "Portugal", "Romania", "Serbia", "Switzerland", "United Kingdom"]
subprocess.call(["C:/Program Files (x86)/NordVPN/NordVPN.exe", "-c", "-g", countries[random.randrange(15)]])
