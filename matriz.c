#include<stdio.h>
#include<stdlib.h>

int main(){
    int valores[4][4], i = 0, j = 0, escolha = 0, matriz = 0;
    int soma1 = 0, soma2 = 0, soma3 = 0, soma4 = 0, somaacima = 0;

    system("cls");
    do{

        printf("==== MENU ====\n");
        printf("1- Cadastrar\n");
        printf("2- Relatorio\n");
        printf("3- Sair\n");
        printf("Escolha um opcao: ");
        scanf("%d", &escolha);

             int c;
             while ((c = getchar()) != '\n' && c != EOF); 

        system("cls");

        switch (escolha){
        
            case 1: 
                for(i = 0; i < 4; i++){
                    printf("==== CADASTRO ====\n");
                    for(j = 0; j < 4; j++){
                        printf("Informe o valor da posicao [%d][%d]: ", i + 1, j + 1);
                        scanf("%d", &valores[i][j]);
                    }
                    system("cls");
                }
                matriz = 1;
                break;

            case 2:
                if(matriz == 1){
                    printf("\n==== RELATORIO ====\n");
                    for(i = 0; i < 4; i++){
                        for(j = 0; j < 4; j++){
                            printf("%4d\t", valores[i][j]);

                            if(i < j){
                                somaacima += valores[i][j];
                            }
                        }
                        printf("\n");

                    }

                    for (i = 0; i < 4; i++) {
                        soma1 += valores[i][0];
                        soma2 += valores[i][1];
                        soma3 += valores[i][2];
                        soma4 += valores[i][3];
                    }

                    printf("\nA soma da coluna 1 e %d\n", soma1);
                    printf("A soma da coluna 2 e %d\n", soma2);
                    printf("A soma da coluna 3 e %d\n", soma3);
                    printf("A soma da coluna 4 e %d\n", soma4);
                    printf("A soma dos valores acima da diagonal principal e %d\n", somaacima);
                    
                    printf("===================\n\n");
                }
                else
                    printf("Nenhuma matriz cadastrada\n\n");

                break;

            case 3:
                printf("\nSaindo do programa...\n\n");
                break;

            default:
                printf("\nOpcao invalida! Escolha uma opcao disponivel!\n\n");
                break;
        
        }
    }while(escolha != 3);

    return 0;
}