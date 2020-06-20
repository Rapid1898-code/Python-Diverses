s = ["200","abc","300","400","500"]

diff_temp = 0
while True:
    shift=False
    for i,cont in enumerate(s):
        if cont[0].isalpha ():
            s.insert(0,"-")
            s.pop()
            diff_temp += 1
            shift=True
    if shift == False: break
print(s)
print (diff_temp)
