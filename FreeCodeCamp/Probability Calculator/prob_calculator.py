import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for i in kwargs:
            for j in range(kwargs[i]):
                self.contents.append(i)

    def draw(self,number):
        if len(self.contents) <= number: return(self.contents)
        """
        tmp_contents = list(self.contents)
        erg = []
        for i in range(number):
            rand = random.randint(0,len(tmp_contents)-1)
            erg.append(tmp_contents[rand])
            del tmp_contents[rand]
        """
        erg = []
        for i in range (number):
            rand = random.randint (0, len (self.contents) - 1)
            erg.append (self.contents[rand])
            del self.contents[rand]
        return(erg)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for i in range(num_experiments):
        tmp_hat = list(hat.contents)
        erg = hat.draw(num_balls_drawn)

        print(erg)

        success = True
        for key, val in expected_balls.items():
            if key not in erg or erg.count(key) < val: success = False
        if success: success_count += 1
        hat.contents = list(tmp_hat)
    return (success_count / num_experiments)



