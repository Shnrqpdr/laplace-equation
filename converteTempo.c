#include <stdlib.h>
#include <stdio.h>

void main() {

    double minuto, segundos, tempo;
    int threads=1;

    FILE *file;

    file = fopen("temposThreadsPessoal.txt", "w+");

    fprintf(file, "tempos\tthreads\n");

    while(threads <= 8){

        printf("\nDigite o tempo em minutos: ");
        scanf("%lf", &minuto);

        printf("\nDigite o tempo em segundos: ");
        scanf("%lf", &segundos);

        minuto = minuto*60;

        tempo = minuto + segundos;

        fprintf(file, "%f %d\n", tempo, threads);

        threads = threads + 1;
    }

    printf("Fim do programa");
    
}