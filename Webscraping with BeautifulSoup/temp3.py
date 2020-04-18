import  subprocess, re, random, datetime

"""
def statusCheck():   
    # This function will run a status check on your nordvpn service to see if you are already connected.  You must be disconnected for this program to work.        
    nord_output = subprocess.Popen (["nordvpn", "status"], stdout=subprocess.PIPE)
    status = re.split ("[\r \n :]", nord_output.communicate ()[0].decode ("utf-8"))[-2]

    if status == "Disconnected":
        return True

    else:
        disconnect = input (
            "You are currently connected to NordVPN already.  Would you like to disconnect and continue? [y/n]: ").lower ()

        if disconnect == "y":
            subprocess.call (["nordvpn", "disconnect"])
            return True

        elif disconnect == "n":
            print ("You have chosen not to disconnect from your current NordVPN session.  Exiting program...")
            exit ()

def getCountries(): 
    # This function will return a list of the current countries with available servers for your nordvpn account.
    nord_output = subprocess.Popen(["nordvpn", "countries"], stdout=subprocess.PIPE)
    countries = re.split("[\t \n]", nord_output.communicate()[0].decode("utf-8"))

    while "" in countries:
        countries.remove("")

    return countries

laender = getCountries()
"""

nord_output = subprocess.Popen(["C:/Program Files (x86)/NordVPN/NordVPN.exe", "countries"], stdout=subprocess.PIPE)