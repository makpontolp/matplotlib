import matplotlib.pyplot as plt


x = [1,2,3,4,5,6,7,8,9]
y = [1,10,2,6,2,4,5,4,1]



titulo = "Meu Primeiro grafico em barras"
ex = "Eixo X"
ey = "Eixo Y"

plt.bar(x,y)
plt.title(titulo)
plt.xlabel(ex)
plt.ylabel(ey)
plt.show()


