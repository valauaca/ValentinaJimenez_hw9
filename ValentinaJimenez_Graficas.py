import numpy as np

import matplotlib.pyplot as plt


#cargar los datos para la grafica

datospython=np.loadtxt('times_python.csv')
datosc=np.loadtxt('times_cpp.csv')

#para separar las columnas n, tiempo 

x1=datospython[:,0]
y1=datospython[:,1]
x2=datosc[:,0]
y2=datosc[:,1]

plt.figure()
a=plt.plot(x1,y1,color='k')
b=plt.plot(x2,y2,color='b', marker='D')
plt.title("Evoluacion temporal de la temperatura")
plt.legend([a,b],["python","c++"])
plt.xlabel("Tiempo (Anios)")
plt.ylabel("Temperatura")
#plt.show()
plt.savefig('temp_analisis.png')







