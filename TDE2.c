#include <stdio.h>    // Para entrada e saída de dados (printf, scanf, fgets)
#include <stdlib.h>   // Para funções do sistema (system, etc.)
#include <string.h>   // Para manipulação de strings (strlen, strstr)
#include <ctype.h>    // Para verificar caracteres (isalpha, isdigit)
#include <time.h>     // Para pegar a data atual do sistema

#define MAX_ESTOQUE 50  // Limite máximo de remédios que podem ser cadastrados

// Remove o caractere '\n' deixado pelo fgets no final da string
void limpar_quebra_linha(char *str){
    size_t len = strlen(str);
    if(len > 0 && str[len - 1] == '\n'){
        str[len - 1] = '\0';
    }
}

// Limpa o buffer do teclado para evitar erros em leituras subsequentes
void limpar_buffer(){
    int c;
    while((c = getchar()) != '\n' && c != EOF);
}

// Verifica se a string contém apenas letras e espaços
int somente_letras(char *str){
    for(int i = 0; str[i] != '\0'; i++){
        if(!isalpha(str[i]) && str[i] != ' '){  // Se tiver algo que não seja letra nem espaço
            return 0;  // Retorna 0 (falso)
        }
    }
    return 1;  // Retorna 1 (verdadeiro)
}

// Estrutura para armazenar uma data (dia, mês e ano)
typedef struct {
    int dia;
    int mes;
    int ano;
} data;

// Estrutura principal que representa um remédio
typedef struct {
    char nome[100];     // Nome do remédio
    char forma[50];     // Forma farmacêutica (ex: comprimido, pomada)
    char dosagem[50];   // Dosagem (ex: 500mg)
    int qtdcaixa;       // Quantidade de caixas em estoque
    data validade;      // Data de validade do remédio
    float valor;        // Valor em reais (R$)
} tipo_remedio;

// Retorna a data atual do sistema
data data_atual(){
    time_t t = time(NULL);          // Pega o tempo atual
    struct tm tm = *localtime(&t);  // Converte para formato de data legível

    data hoje;
    hoje.dia = tm.tm_mday;
    hoje.mes = tm.tm_mon + 1;       // Mês começa em 0, então soma +1
    hoje.ano = tm.tm_year + 1900;   // Ano começa em 1900, então soma +1900

    return hoje;
}

// Verifica se uma data informada é válida
int data_valida(int d, int m, int a) {
    int dias_mes[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};

    // Ano mínimo é 2025 e o mês deve estar entre 1 e 12
    if (a < 2025 || m < 1 || m > 12) return 0;

    // Ajuste para ano bissexto (fevereiro tem 29 dias)
    if (m == 2 && ((a % 4 == 0 && a % 100 != 0) || (a % 400 == 0)))
        dias_mes[2] = 29;

    // Verifica se o dia é válido para o mês
    if (d < 1 || d > dias_mes[m]) return 0;

    return 1; // Data válida
}

int main(){
    tipo_remedio estoque[MAX_ESTOQUE]; // Vetor de remédios
    data hoje = data_atual();           // Pega a data atual
    int i, escolha, escolha1, escolha2;
    int qtdremedios, cadastro = 0, senha, parou = 0, qtdestoque, validos;
    int mes_diff;

    system("cls"); // Limpa a tela

    do{
        // --- MENU PRINCIPAL ---
        printf("==== MENU ====\n");
        printf("1 - Farmaceutico\n");
        printf("2 - Cliente\n");
        printf("3 - Sair\n");
        printf("Escolha uma opcao acima: ");
        scanf("%d", &escolha);
        limpar_buffer();

        system("cls");

        switch(escolha){
        // --- MODO FARMACÊUTICO ---
        case 1:
            senha = 0;
            printf("Digite a senha: ");
            scanf("%d", &senha);
            limpar_buffer();
            system("cls");

            // --- Verifica se a senha está correta ---
            if(senha == 2025){
                do{
                    // --- MENU FARMACÊUTICO ---
                    printf("==== MENU FARMACEUTICO ====\n");
                    printf("1 - Cadastrar remedios\n");
                    printf("2 - Ver estoque\n");
                    printf("3 - Sair\n");
                    printf("Escolha uma opcao acima: ");
                    scanf("%d", &escolha1);
                    limpar_buffer();
                    system("cls");

                    switch(escolha1){
                    // --- CADASTRO DE REMÉDIOS ---
                    case 1:
                        qtdremedios = 0;

                        // Usuário informa quantos remédios deseja cadastrar
                        do{
                            printf("Informe a quantidade de remedios que deseja cadastrar: ");
                            scanf("%d", &qtdremedios);
                            limpar_buffer();

                            if(qtdremedios <= 0){
                                printf("\nQuantidade invalida! Digite novamente.\n");
                            }
                        }while(qtdremedios <= 0);
                        system("cls");

                        qtdestoque = parou + qtdremedios;  // Define até onde preencher no vetor

                        // --- LOOP PARA CADASTRAR CADA REMÉDIO ---
                        for(i = parou; i < qtdestoque; i++){
                            system("cls");
                            printf("Remedio %d:\n", i + 1);

                            // --- NOME ---
                            do{
                                printf("Informe o nome do remedio: ");
                                fgets(estoque[i].nome, 100, stdin);
                                limpar_quebra_linha(estoque[i].nome);

                                if(!isalpha(estoque[i].nome[0])){
                                    printf("\nO nome deve comecar com uma letra! Digite novamente.\n");
                                }
                            }while(!isalpha(estoque[i].nome[0]));

                            // --- FORMA FARMACÊUTICA ---
                            do{
                                printf("Informe a forma farmaceutica do remedio (Ex: comprimido): ");
                                fgets(estoque[i].forma, 50, stdin);
                                limpar_quebra_linha(estoque[i].forma);

                                if(!somente_letras(estoque[i].forma)){
                                    printf("\nA forma deve conter apenas letras e espacos! Digite novamente.\n");
                                }
                            }while(!somente_letras(estoque[i].forma));

                            // --- DOSAGEM ---
                            do{
                                printf("Informe a dosagem do remedio (Ex: 500mg ou 10ml): ");
                                fgets(estoque[i].dosagem, 50, stdin);
                                limpar_quebra_linha(estoque[i].dosagem);

                                // Verifica se a dosagem contém unidade válida
                                if(!(strstr(estoque[i].dosagem, "mg") || strstr(estoque[i].dosagem, "ml") ||
                                     strstr(estoque[i].dosagem, "g") || strstr(estoque[i].dosagem, "l"))){
                                    printf("\nUnidade de medida invalida!\n");
                                }

                                // Verifica se começa com um número
                                if(!isdigit(estoque[i].dosagem[0])){
                                    printf("\nA dosagem deve comecar com um numero! Digite novamente.\n");
                                }

                            }while(!isdigit(estoque[i].dosagem[0]) && 
                                   (!(strstr(estoque[i].dosagem, "mg"))) || 
                                   (!(strstr(estoque[i].dosagem, "mg") || strstr(estoque[i].dosagem, "ml") || 
                                   strstr(estoque[i].dosagem, "g") || strstr(estoque[i].dosagem, "l"))));

                            // --- DATA DE VALIDADE ---
                            do{
                                printf("Informe a data de validade do remedio (dd/mm/aaaa): ");
                                validos = scanf("%d/%d/%d", &estoque[i].validade.dia, &estoque[i].validade.mes, &estoque[i].validade.ano);
                                limpar_buffer();

                                if(validos != 3){
                                    printf("\nA data deve conter barras (Ex: 07/11/2025).\n");
                                }                                
                                else if(!data_valida(estoque[i].validade.dia, estoque[i].validade.mes, estoque[i].validade.ano)){
                                    printf("Data invalida! Digite novamente.\n\n");
                                }
                            }while(!data_valida(estoque[i].validade.dia, estoque[i].validade.mes, estoque[i].validade.ano) || (validos != 3));

                            // --- VALOR ---
                            do{
                                printf("Informe o valor do remedio (R$): ");
                                scanf("%f", &estoque[i].valor);
                                limpar_buffer();

                                if(estoque[i].valor <= 0){
                                    printf("\nValor invalido! Digite novamente.\n");
                                }
                            }while(estoque[i].valor <= 0);

                            // --- QUANTIDADE DE CAIXAS ---
                            do{
                                printf("Informe a quantidade de caixas: ");
                                scanf("%d", &estoque[i].qtdcaixa);
                                limpar_buffer();

                                if(estoque[i].qtdcaixa <= 0){
                                    printf("\nQuantidade invalida! Digite novamente.\n");
                                }
                            }while(estoque[i].qtdcaixa <= 0);

                            system("pause");
                            system("cls");

                            cadastro = 1;  // Marca que há remédios cadastrados
                            parou += 1;    // Atualiza o índice de parada
                        }
                        break;

                    // --- VISUALIZAR ESTOQUE ---
                    case 2:
                        if(cadastro == 1){
                            system("cls");
                            printf("\n==== ESTOQUE ====\n");
                            data hoje = data_atual();

                            for(i = 0; i < parou; i++){
                                // Calcula diferença de meses entre validade e hoje
                                mes_diff = (estoque[i].validade.ano - hoje.ano) * 12 + 
                                           (estoque[i].validade.mes - hoje.mes);

                                // Exibe informações
                                printf("Remedio %d: \n", i + 1);
                                printf("Nome: %s\n", estoque[i].nome);
                                printf("Forma: %s\n", estoque[i].forma);
                                printf("Dosagem: %s\n", estoque[i].dosagem);
                                printf("Data Validade: %02d/%02d/%04d\n", estoque[i].validade.dia, estoque[i].validade.mes, estoque[i].validade.ano);
                                printf("Valor: %.2f\n", estoque[i].valor);
                                printf("Caixas: %d\n\n", estoque[i].qtdcaixa);

                                // Verifica estoque baixo
                                if(estoque[i].qtdcaixa <= 2)
                                    printf("Necessario reposicao de unidades!\n");

                                // Verifica se está vencido ou perto de vencer
                                if((estoque[i].validade.ano < hoje.ano) ||
                                   (estoque[i].validade.ano == hoje.ano && estoque[i].validade.mes < hoje.mes) ||
                                   (estoque[i].validade.ano == hoje.ano && estoque[i].validade.mes == hoje.mes && estoque[i].validade.dia < hoje.dia))
                                    printf("Remedio vencido!\n\n");
                                else if(mes_diff >= 0 && mes_diff <= 1)
                                    printf("Validade perto de expirar!\n\n");
                            }

                            system("pause"); // Pausa a tela até o usuário apertar enter
                            system("cls");
                        } else {
                            printf("Nenhum remedio cadastrado ainda!\n");
                            system("pause");
                            system("cls");
                        }
                        break;

                    // --- SAIR DO MENU FARMACÊUTICO ---
                    case 3:
                        printf("Saindo do menu farmaceutico...\n");
                        system("pause");
                        system("cls");
                        break;

                    // --- OPÇÃO INVÁLIDA ---
                    default:
                        printf("Opcao invalida! Escolha uma opcao valida!\n");
                        system("pause");
                        system("cls");
                        break;
                    }
                }while(escolha1 != 3);
            }
            else {
                // --- Senha incorreta ---
                printf("Senha invalida!\n");
                system("pause");
                system("cls");
            }
            break;

        // --- MODO CLIENTE ---
        case 2:
            do{
                printf("==== MENU CLIENTE ====\n");
                printf("1 - Ver estoque\n");
                printf("2 - Sair\n");
                printf("Escolha uma opcao acima: ");
                scanf("%d", &escolha2);
                limpar_buffer();
                system("cls");

                switch(escolha2){
                // Exibe o estoque
                case 1:
                    if(cadastro == 1){
                        system("cls");
                        printf("\n==== ESTOQUE ====\n");
                        for(i = 0; i < parou; i++){
                            printf("Remedio %d: \n", i + 1);
                            printf("Nome: %s\n", estoque[i].nome);
                            printf("Forma: %s\n", estoque[i].forma);
                            printf("Dosagem: %s\n", estoque[i].dosagem);
                            printf("Data Validade: %02d/%02d/%04d\n", estoque[i].validade.dia, estoque[i].validade.mes, estoque[i].validade.ano);
                            printf("Valor: %.2f\n", estoque[i].valor);
                            printf("Caixas: %d\n\n", estoque[i].qtdcaixa);
                        }
                        system("pause");
                        system("cls");
                    }
                    else{
                        printf("Nenhum remedio cadastrado ainda!\n");
                        system("pause");
                        system("cls");
                    }
                    break;

                // Sai do menu do cliente
                case 2:
                    printf("Saindo do menu cliente...\n");
                    system("pause");
                    system("cls");
                    break;

                // Caso digite opção inválida
                default:
                    printf("\nOpcao invalida! Escolha uma opcao valida!\n");
                    system("pause");
                    system("cls");
                    break;
                }
            }while(escolha2 != 2);
            break;

        // --- SAIR DO PROGRAMA ---
        case 3:
            printf("Saindo do programa...\n");
            break;

        // Caso digite algo inválido no menu principal
        default:
            printf("Opcao invalida! Escolha uma opcao valida!\n");
            system("pause");
            system("cls");
            break;
        }

    }while(escolha != 3); // Repete até o usuário escolher “Sair”
    return 0;
}