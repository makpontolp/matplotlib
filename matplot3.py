import matplotlib.pyplot as plt

x1 = [1,3,5,7,9,11,13,15]
y1 = [1,5,2,6,2,4,5,4]

x2 = [0,2,4,6,8,10,12,14]
y2 = [3,3,6,8,10,14,9,3]

plt.bar(x1,y1, label = "Grupo Azul")
plt.bar(x2,y2, label = "Grupo Laranja")
plt.legend()
plt.show()

