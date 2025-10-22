#include<stdio.h>
#include<stdlib.h>


int main(){
    int a,b,c;


    printf("Qual o valor de A: ");
    scanf("%d", &a);
    printf("Qual o valor de B: ");
    scanf("%d", &b);


    c = b;
    b = a;
    a = c;


    printf("O valor de A e: %d. E o valor de B e: %d \n", a, b);


    return 0;
}