#include <iostream>

using std::cout;
using std::endl;


// declarar funciones 

int fibonacci(int N);

float get_time(int N);

//la funcion recursiva es la que se llama a si misma, se utilizan factoriales para hallar factoriales
//

int fibonacci(int N) {

	//primero se define el caso base en el que la funcion es igual a n

	if( N==0 || N==1){

		return N;
	}
	// aqui ya es el recursivo, la funcion es igual a la funcion en n-1 y en n-2

	else{
	// declara la variable donde se va a guardar la funcion fibonacci
		int funcion;

		funcion=fibonacci(N-1)+fibonacci(N-2);
		return funcion;

	}
		
}

float get_time(int N){

	clock_t t;
	t = clock();
	fibonacci(N);
	// saca el tiempo que se demora en hacer la funcion fibonacci
	t = clock() - t;
	float time = ((float)t)/CLOCKS_PER_SEC;

}



//aqui se ejecuta las funciones declaradas al inicio 

int main(){

	int n=20;

	cout <<"La serie de Fibonacci es:"<< fibonacci(n) << endl;

	int N=0;
	while(N<=35){

	
	cout<< N <<","<< get_time(n) << endl;
	N++;

	}
	return 0;

}

	

	


