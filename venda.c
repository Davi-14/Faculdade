#include<stdio.h>
#include<stdlib.h>


int main(){
    int quantidade;
    float valor, valorfinal, imposto;


    printf("Qual a quantidade de produtos: ");
    scanf("%d", &quantidade);
    printf("Qual o valor o valor dos produtos (R$): ");
    scanf("%f", &valor);
    printf("Qual o imposto que sera cobrado: (%%)");
    scanf("%f", &imposto);


    valorfinal = (quantidade * valor) + (quantidade * valor) * ( imposto / 100);


    printf("O valor final com o imposto e: %.2f \n", valorfinal);


    return 0;
}