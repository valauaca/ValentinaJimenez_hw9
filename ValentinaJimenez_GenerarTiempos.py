import numpy as np

# funcion fibonacci

def fibonacci(N):

	# condicion del caso base

	if(N==0 or N==1):

		return N

	# esto es para el caso recursivo

	else:

		funcion=fibonacci(N-1)+fibonacci(N-2)
		return funcion

# funcion que da el tiempo que tarda la funcion fibonacci para un entero N
def get_time(N):

	import time
	t0 = time.time()
	fibonacci(N)
	t1 = time.time()-t0
	return t1

# el while es necesario para que no lo haga infinitas veces, de esta manera lo tenemos para los N menores a 25
N=0;
while(N<=25):

	print N, ",", get_time(N)
	N+=1



