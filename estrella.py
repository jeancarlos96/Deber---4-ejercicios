import turtle
t=turtle.Pen()
print ("Dibuja estrella con numeros de puntas IMPARES")
x=int(input("Ingrese el número de puntas de la estrella: "))

def estrella(lados):
	prod=360/x
	grado=(prod*2)
	for a in range (1, x+1):
		t.forward(100)
		t.right(grado)

star=estrella(x)
#sssprint(star)
turtle.getscreen()._root.mainloop()