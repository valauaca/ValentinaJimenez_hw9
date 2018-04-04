import numpy as np

import matplotlib.pyplot as plt


#cargar los datos para la grafica

datospython=np.loadtxt('times_python.csv')
datosc=np.loadtxt('times_cpp.csv')

#para separar las columnas n, 

x1=datospython[:,0]
y1=datospython[:,1]
x2=datosc[:,0]
y2=datosc[:,1]

plt.figure()
a=plt.plot(x1,y1,color='k')
b=plt.plot(x2,y2,color='b', marker='D')
plt.title("cpp vs python")
plt.legend([a,b],["python","c++"])
plt.xlabel("N")
plt.ylabel("tiempo")
#plt.show()
plt.savefig('cpp_vs_python.png')







