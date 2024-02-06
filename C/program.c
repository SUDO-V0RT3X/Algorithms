#include <stdio.h>
#include <stdlib.h>

int main(){

	//printf("Hello, World!\n");
	//printf("\n\nMy program");
	
	char letter = 'm';
	//printf("letter \n %c",letter);
	
	char word[] = "hello";
	//printf("a word %s",word);
	
	short numberOne = 9;
	int numberTwo = 10;
	long numberThree = 110;
	long long numberFour = 12000;
	
	float numberFive = 1.2;
	double numberSix = 3.9;
	long double numberSeven = 100.809;
	
	const char CANT_CHANGE[] = "goodbye";
	//printf("a const: %s \n" ,CANT_CHANGE);

	//printf("A letter: %c \n A word: %s \n A short: %i \n An int: %i \n A long: %i \n A long long:%i \n A float: %f \n A double: %f \n A long double: %Lf \n A constant: %s ", letter, word, numberOne, numberTwo, numberThree, numberFour, numberFive, numberSix, numberSeven, CANT_CHANGE);
	
	printf("a letter: " + letter);
	//printf("a number: " + numberTwo);

	//printf("%d is actually float with a value of 55.65 ", (int)55.65);
	//printf("%f", 3 / 2);

	return 0;
}

