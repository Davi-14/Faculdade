#include<stdio.h>
#include<stdlib.h>


int main(){
    float media,n1,n2;


    printf("Informe as notas da avaliacoes: ");
    scanf("%f%f", &n1,&n2);


    media = (n1 + n2) / 2;


    if(media >= 7 && media < 10){
        printf("Aprovado \n");
    }
    else if(media == 10){
        printf("Aprovado com distincao \n");
    }
    else if(media >= 3 && media < 7){
        printf("Exame \n");
    }
    else{
        printf("Reprovado \n");
    }
    return 0;
}