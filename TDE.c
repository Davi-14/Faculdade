#include <stdio.h>
#include <stdlib.h>

int main(){
    int alunos = 0, i, escolha, aluno;
    float nota[30], soma, mediag, maior, menor;
    int acima, abaixo, media;

    do {
        printf("\n======= MENU =======\n");
        printf("1. Cadastrar notas\n");
        printf("2. Exibir relatorio\n");
        printf("3. Pesquisar nota\n");
        printf("4. Sair\n");
        printf("====================\n\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &escolha);

        switch (escolha){
            case 1:
                printf("Informe a quantidade de alunos (5 a 30): ");
                scanf("%d", &alunos);

                if (alunos < 5 || alunos > 30){
                    printf("Quantidade invalida!\n");
                    alunos = 0;
                } 
                else {
                    for (i = 0; i < alunos; i++){
                        do{
                        printf("Informe a nota do aluno %d: ", i + 1);
                        scanf("%f", &nota[i]);

                        if(nota[i] < 0 || nota[i] > 10){
                            printf("Nota invalida!\n");
                        }
                        } while (nota[i] < 0 || nota[i] > 10);
                    }
                }
                break;
            case 2:
                if (alunos == 0){
                    printf("Nenhuma nota cadastrada!\n");
                } 
                else {
                    soma = 0;
                    maior = nota[0];
                    menor = nota[0];
                    acima = 0;
                    abaixo = 0;

                    for (i = 0; i < alunos; i++){
                        soma += nota[i];
                        if (nota[i] > maior) maior = nota[i];
                        if (nota[i] < menor) menor = nota[i];
                    }

                    mediag = soma / alunos;
                    media = 7;

                    for (i = 0; i < alunos; i++){
                        if (nota[i] >= media)
                            acima++;
                        else
                            abaixo++;
                    }

                    printf("\n====== RELATORIO ======\n");
                    printf("A media para passar de ano e %d\n", media);
                    printf("Media geral da turma: %.2f\n", mediag);
                    printf("Maior nota: %.2f\n", maior);
                    printf("Menor nota: %.2f\n", menor);
                    printf("Alunos acima da media: %d\n", acima);
                    printf("Alunos abaixo da media: %d\n", abaixo);
                    printf("\n=======================\n");
                }
                break;
                case 3:
                if(alunos == 0){
                    printf("Alunos nao cadastrado! \n\n");
                    break;
                }
                    printf("informe qual o aluno deseja pesquisar: ");
                    scanf("%d", &aluno);
                if(aluno < 0 || aluno > alunos){
                    printf("Aluno inexistente! \n");
                }
                else{
                    printf("A nota do aluno %d e %.2f \n", aluno, nota[aluno - 1]);
                }
                break;
                case 4:
                    printf("\nSaindo do programa...\n");
                    break;
                default:
                    printf("\nOpcao invalida! \n");
        }
    } while (escolha != 4);

    return 0;
}