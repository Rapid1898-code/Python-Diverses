def arithmetic_arranger(problems, arg=False):
    result = ["","","",""]
    if len(problems) > 5: return("Error: Too many problems.")
    for idx, i in enumerate(problems):
      if "*" in i or "/" in i:
        return("Error: Operator must be '+' or '-'.")
      if i.replace("+","").replace("-","").replace(" ","").isdigit() == False:
        return("Error: Numbers must only contain digits.")
      if "+" in i:
        arith = "+"
        nr1 = i.split("+")[0].strip()
        nr2 = i.split("+")[1].strip()
        erg = str(int(nr1) + int(nr2))
      elif "-" in i:
        arith = "-"
        nr1 = i.split("-")[0].strip()
        nr2 = i.split("-")[1].strip()
        erg = str(int(nr1) - int(nr2))
      if len(nr1) > 4 or len(nr2) > 4:
        return("Error: Numbers cannot be more than four digits.")

      # same length for both numbers
      if len(nr1) > len(nr2):
        max_len = len(nr1)
        while len(nr1) != len(nr2): nr2 = " " + nr2
      else:
        max_len = len(nr2)
        while len(nr1) != len(nr2): nr1 = " " + nr1

      result[0] = result[0] + "  " + nr1
      result[1] = result[1] + arith + " " + nr2
      result[2] = result[2] + "--" + "-"*len(nr1)

      if len(problems) > 1 and arg == True:
        while max_len + 2 > len(erg): erg = " " + erg
        result[3] = result[3] + erg

      if idx != len(problems)-1:
        for x in range(4):
          if x <= 2: result[x] = result[x] + "    "
          elif len(problems) > 1 and arg == True: result[x] = result[x] + "    "

    for i in range (4): print(result[i])

    if arg == True: arranged_problems = result[0] + "\n" + result[1] + "\n" + result[2] + "\n" + result[3]
    else: arranged_problems = result[0] + "\n" + result[1] + "\n" + result[2]

    return arranged_problems

#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)


