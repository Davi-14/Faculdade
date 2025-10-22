#include<stdio.h>
#include<stdlib.h>


int main(){
    int n1,n2;


    printf("Informe dois numeros: ");
    scanf("%d%d", &n1,&n2);


    if (n1 > n2){
        printf("%d e o maior numero \n", n1);
    }
    else{
        printf("%d e o maior numero \n", n2);
    }


    return 0;
}