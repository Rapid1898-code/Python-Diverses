class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def __str__(self):
        l = (30 - len(self.name)) // 2
        erg = l * "*" + self.name + l * "*"
        if len (erg) == 29: erg += "*"
        erg += "\n"
        for i in self.ledger:
            am = str(i["amount"])
            desc = i["description"]
            if len(desc) > 23: desc = desc[:23]
            if "." not in am: am += ".00"
            am = " "*(7-len(am)) + am
            erg += desc + " "*(23-len(desc)) + am + "\n"
        bal = 0
        for i in self.ledger: bal += i["amount"]
        erg += "Total: " + str(bal)
        return (erg)

    def check_funds(self,val):
        bal = 0
        for i in self.ledger: bal += i["amount"]
        if bal >= val: return(True)
        else: return(False)

    def deposit(self,val,desc=""):
        self.ledger.append({"amount": val, "description": desc})

    def get_balance(self):
        bal = 0
        for i in self.ledger: bal += i["amount"]
        return(bal)

    def withdraw(self,val,desc=""):
        if self.check_funds(val):
            self.ledger.append({"amount": val*(-1), "description": desc})
            return(True)    # withdrawel possible
        else: return(False)   # withdrawel NOT possible

    def transfer(self,val,cat):
        if self.check_funds(val):
            desc1 = "Transfer to " + cat.name
            self.ledger.append({"amount": val*(-1), "description": desc1})
            desc2 = "Transfer from " + self.name
            cat.ledger.append({"amount": val, "description": desc2})
            return(True)    # transfer possible
        else: return(False)   # transfer NOT possible

def create_spend_chart(categories):
    wd = []
    perc = []
    for i in categories:
        temp_wd = 0
        for j in i.ledger:
            if j["amount"] < 0: temp_wd += j["amount"]
        wd.append(temp_wd * (-1))
    for i in wd:
        perc.append(int(i / sum(wd) * 100 / 10))

    erg = "Percentage spent by category\n"
    for i in range(100,-1,-10):
        if len(str(i)) == 2: line = " " + str(i)
        elif len(str(i)) == 1: line = "  " + str(i)
        else: line = str(i)
        line += "|"
        for j_idx, j_cont in enumerate(perc):
            if j_cont >= i/10:
                if j_idx == 0: line += " o"
                else: line += "  o"
            else:
                if j_idx == 0: line += "  "
                else: line += "   "
        erg += line + "  " + "\n"
    erg += "    -" + "---"*len(perc) + "\n"

    names = []
    for i in categories: names.append(i.name)

    max_len = len(max(names, key=len))
    for i in range (max_len):
        line = "     "
        for j in categories:
            if i > len(j.name)-1: line += "   "
            else: line += j.name[i] + "  "
        if i < max_len -1: erg += line + "\n"
        else: erg += line

    return(erg)


