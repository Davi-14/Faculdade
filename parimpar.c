#include<stdio.h>
#include<stdlib.h>

int main(){
    int numero;

    printf("Digite um numero: ");  
    scanf("%d", &numero);

    if((numero % 2) != 0){
        printf("%d e impar \n", numero);
    }
    else{
        printf("%d e par \n", numero);
    }

    return 0;
}