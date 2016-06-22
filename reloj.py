import time 
# RELOJ .... TIEMPO REAL ...¡¡¡
t= time.localtime()
s=t[4]
print ("Reloj")
for s in range (0,25):
	print("Hora .....: ") #Imprime la hora cada 60 minutos
	print(s)
	for s in range (0,61):
		print ("Minuto....: ") # imprime los minutos cada 60 segundos
		print(s)
		for s in range (1,61):
			print("Seg:" ) # imprime los segundos en tiempo real...
			print(s)
			time.sleep(1) # hace que cada linea se imprima en un tiempo determinado