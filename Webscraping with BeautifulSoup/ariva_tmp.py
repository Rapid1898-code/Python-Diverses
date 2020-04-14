from itertools import zip_longest

l = [[1,2,3,4,5,6],[7,8,9],[10,11,12]]

#print(list(map(list,zip(*l))))
r = [list(filter(None,i)) for i in zip_longest(*l)]
print(r)
