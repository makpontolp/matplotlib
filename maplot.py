import matplotlib.pyplot as plt


x = [1,2,3,4,5,6,7,8,9]
y = [1,10,2,6,2,4,5,4,1]


plt.plot(x,y)
titulo = "Meu Primeiro grafico"
ex = "Eixo X"
ey = "Eixo Y"
plt.title(titulo)
plt.xlabel(ex)
plt.ylabel(ey)
plt.show()


plt.bar(x,y)
plt.title(titulo)
plt.xlabel(ex)
plt.ylabel(ey)
plt.show()




x1 = [1,3,5,7,9,11,13,15]
y1 = [1,5,2,6,2,4,5,4]

x2 = [0,2,4,6,8,10,12,14]
y2 = [3,3,6,8,10,14,9,3]

plt.bar(x1,y1, label = "Grupo Azul")
plt.bar(x2,y2, label = "Grupo Laranja")
plt.legend()
plt.show()



plt.scatter(x1,y1, label = "Grafico de Dipersão", color = "k")
plt.title("ScatterPlot")
plt.scatter(x2,y2)
plt.show()




plt.title("Scatterplot + plot (Grafico de Dispersão)")
plt.scatter(x1,y1, label = "Pontos Azuis")
plt.plot(x1,y1)
plt.legend()

plt.scatter(x2,y2, label = "Pontos Cinzas", color = 'gray')
plt.plot(x2,y2, color = 'gray')
plt.legend()


plt.show()



plt.scatter(x2,y2, label = "Pontos Cinzas", color = 'gray', marker = "s")
plt.title("Trocando marcador")
plt.plot(x2,y2, color = 'gray')
plt.legend()
plt.show()


plt.scatter(x2,y2, label = "Pontos Cinzas", color = 'r', marker = "h", s=10)
plt.plot(x2,y2, color = 'k', linestyle="--")
plt.legend()
plt.show()



z = [20,30,40,50,60,70,80,90]

plt.scatter(x2,y2, label = "Pontos Cinzas", color = 'r', marker = "h", s=z)
plt.plot(x2,y2, color = 'k', linestyle="--")
plt.legend()
plt.show()


# z = Represeta do tamanho do plot (Definido por uma lista)

