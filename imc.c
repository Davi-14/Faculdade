#include<stdio.h>
#include<stdlib.h>

int main(){
	float mediag, imc[100], peso[100], altura[100], soma = 0;
	int i, escolha, pessoas;
	do {
		printf("\n==== MENU ====\n");
		printf("1. Cadastro \n");
		printf("2. Relatorio \n");
		printf("3. Sair \n");
		printf("Escolha uma das opcoes acima: ");
		scanf("%d", &escolha);
		
		switch(escolha){
			case 1:
				printf("\nInforme a quantidade de pessoas que desejam calcular o imc: ");
				scanf("%d", &pessoas);
			
				for (i = 0; i < pessoas; i++){
					printf("\nInforme a altura da pessoa %d: ", i + 1);
					scanf("%f", &altura[i]);
					printf("Informe o peso da pessoa %d: ", i + 1);
					scanf("%f", &peso[i]);
					
					imc[i] = peso[i] / (altura[i] * altura[i]);
					
					if (imc[i] < 18.5){
						printf("\nA pessoa %d esta abaixo do peso! \n\n", i + 1);
					}
					else if (imc[i] >= 18.5 && imc[i] < 25){
						printf("\nA pessoa %d esta no peso ideal! \n\n", i + 1);
					}
					else if (imc[i] >= 25 && imc[i] <30){
						printf("\nA pessoa %d esta acima do peso! \n\n", i + 1);
					}
					else if (imc[i] >= 30 && imc[i] < 35){
						printf("\nA pessoa %d esta na obesidade 1! \n\n", i + 1);
					}
					else if (imc[i] >= 35 && imc[i] < 40){
						printf("\nA pessoa %d na obesidade 2! \n\n", i + 1);
					}
					else {
						printf("\nA pessoa %d esta na obesidade morbida! \n\n", i + 1);
					}
					
				}
				break;
				
				case 2:
					soma = 0;
					for (i = 0; i < pessoas; i++){
						soma += imc[i];
				}
				
				mediag = soma / pessoas;
				
				printf("\n==== RELATORIO ====\n");
				printf("A media geral e %.2f \n", mediag);
				
				break;
				
				case 3:
					printf("\nSaindo do programa...\n");
					break;
					
				default:
					printf("Opcao invalida! \n");
		}
		
	} while (escolha != 3);
	
    return 0;
}