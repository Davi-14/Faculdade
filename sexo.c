#include<stdio.h>

int main () {
	int idade[10];
	char sexo[10];
	int i, somam = 0, somaf = 0, qtdf = 0, qtdm = 0, escolha = 0, mvelho = 0, fjovem = 201, ivelho = 0, ijovem = 0, cadastrou = 0, mediam = 0, mediaf = 0;

    do{
        printf("\n==== MENU ====\n");
        printf("1- Cadastrar\n");
        printf("2- Relatorio\n");
        printf("3- Sair\n");
        printf("Escolha um opcao: ");
        scanf("%d", &escolha);

        switch (escolha){
            case 1:
                for(i = 0; i < 10; i++){
                    printf("\nInforme a idade da pessoa %d: ", i + 1);
                    scanf("%d", &idade[i]);

                    while(idade[i] < 0 || idade[i] > 200){
                        printf("Idade invalida! Digite novamente: ");
                        scanf("%d", &idade[i]);
                    }

                    printf("Informe o sexo da pessoa %d (m/f): ", i + 1);
                    scanf(" %c", &sexo[i]);

                    while(sexo[i] != 'm' && sexo[i] != 'f'){
                        printf("Sexo invalido! Digite novamente:");
                        scanf(" %c", &sexo[i]);
                    }

                    cadastrou = 1;
                }
                break;

            case 2:
                if(cadastrou == 0){
                    printf("\nNenhuma pessoa cadastrada!\n");
                }
                else {
                    for(i = 0; i < 10; i++){
                        if(sexo[i] == 'm'){
                            somam += idade[i];
                            qtdm++;
                        }
                        else if(sexo[i] == 'f'){
                            somaf += idade[i];
                            qtdf++;
                        }
                    }
                    for(i = 0; i < 10; i++){
                        if(sexo[i] == 'm'){
                            if(idade[i] > mvelho){
                                mvelho = idade[i];
                                ivelho = i + 1;
                            }
                        }
                        else if(sexo[i] == 'f'){
                            if(idade[i] < fjovem){
                                fjovem = idade[i];
                                ijovem = i + 1;
                            }
                        }
                    }

                    if(qtdm > 0){
                    mediam = somam / qtdm;
                    } 
                    else
                    mediam = 0;

                    if(qtdf > 0){
                    mediaf = somaf / qtdf;
                    }
                    else
                    mediaf = 0;

                    printf("\n==== RELATORIO ====\n");
                        printf("A media de idade do sexo (m) e %d\n", mediam);
                        printf("A media de idade do sexo (f) e %d\n", mediaf);

                    if(qtdm > 0){
                        printf("O homem mais velho e o numero %d com %d\n", ivelho, mvelho);
                    }
                    else
                        printf("Nenhum homem cadastrado!\n");

                    if(qtdf > 0){
                        printf("A mulher mais jovem e a numero %d com %d\n", ijovem, fjovem);
                    }
                    else
                        printf("Nenhuma mulher cadastrada!\n");
                }

                    break;

                case 3:
                    printf("\nSaindo do programa...\n");
                    break;

                default:
                    printf("\nOpcao invalidada\n");
        }
    } while(escolha != 3);
	return 0;
}