#include<stdio.h>

int main(){
	int a[10];
	int b[10];
	int i = 0;
	
	for(i = 0;i < 10;i++){
        printf("Informe numero %d: ", i + 1);
		scanf("%d", &a[i]);
		
		b[i] = a[i] * i;
	}

	printf("\n");

	for(i = 0; i < 10; i++) {
    printf("%d, %d\n", a[i], b[i]);
	}	
	
	return 0;
}