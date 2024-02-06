#include <stdio.h>

int main() {
  /*
  printf("Hello World!\n\t");
  printf("bruhh");
  int myInt;
  myInt = 50;
  // comments

  /*mult
  line
  comment*/

  /*
    printf(
        "\n1\t2\t3\n4\t5\t6\n7\t8\t9\n\t0"); // escape sequence ==> a 'command'.
    =
                                             // backsplash + letter

    char Name[] = "vortex"; // string      %s

    int age = 19;        // integers    %d
    double height = 1.7; // fraction      %f
    char Initials = 'M'; // char - ingle quotes    %c

    printf("\n\n%d", 500); // format specifier

    printf("\n%s\t %d\t %f\t %c", Name, age, height, Initials);
  */

  const char hello[] =
      "HELLO"; // consts must be named in capitol. printing a  random string/int
               // without a variable in printf is also considered a constant
  printf(hello);
  return 0;
}
