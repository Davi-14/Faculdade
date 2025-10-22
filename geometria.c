#include<stdio.h>
#include<stdlib.h>
#include<math.h>


int main(){
    int a,b,c,area,areab,areal,areat,areat2,volume,volume2,volume3,raio,altura;
    float pi;


    pi = 3.14;


    printf("Digite o valor dos lados do paralelepipedo: ");
    scanf("%d%d%d", &a,&b,&c);
    volume = a * b * c;
    areat = (2 * a * b) + (2 * b * c) + (2 * a * c);


    printf("Digite o valor da area lateral, area da base e a altura do cilindro: ");
    scanf("%d%d%d", &areal,&areab,&altura);
    areat2 = 2 * areab + areal;
    volume2 = areab * altura;


    printf("Digite o valor do raio da esfera: ");
    scanf("%d", &raio);
    volume3 = (4 * pi * (raio * raio * raio)) / 3;
    area = 4 * pi * (raio * raio);


    printf("O volume e a area total do paralelepido e: %d e %d \n", volume,areat);
    printf("O volume e a area total do cilindro e: %d e %d \n", areat2, volume2);
    printf("O volume e a area da esfera e: %d e %d \n", volume3, area);


    return 0;
}