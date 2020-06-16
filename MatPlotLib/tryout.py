import matplotlib.pyplot as plt

x_values = list(range(1000))
squares = [x**2 for x in x_values]
plt.scatter(x_values, squares, s=5)
plt.xlabel("X-Axe", fontsize=18)                              # X-Axe title with fontsize = 18
plt.ylabel("Y-Axe", fontsize=18)                              # Y-Axe title with fontsize = 18
plt.axis([0,1100,0,1100000])
plt.scatter(x_values, squares, c=squares, cmap=plt.cm.Blues, edgecolor="none", s=10)
plt.scatter(x_values[0],squares[0],c="green",edgecolor="none", s=100)
plt.scatter(x_values[-1],squares[-1],c="red",edgecolor="none", s=100)
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)
plt.figure(dpi=128, figsize=(10,6))
plt.show()
plt.savefig("example.png",bbox_inches="tight")
