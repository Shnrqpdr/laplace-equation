#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Declarações e constantes

#define N 1002
#define tolerance 0.1
#define maxIt 10000000
#define errorTolerance 1e-8
#define potencialInterno -50.0
#define potencialExterno 100.0
#define raioInterno 1.0
#define raioExterno 3.0
#define theta 0.4

// Dimensões da malha

#define xInicial -5.0
#define xFinal 5.0
#define yInicial -5.0
#define yFinal 5.0

void setContour(double **v, double dx, double dy){
    double x, y, r;

    for(int i = 0; i < N/2; i++){
        for(int j = 0; j < N/2; j++){
            x = xInicial + i*dx;
            y = yInicial + j*dy;
            r = sqrt(x*x + y*y);

            if(fabs(raioExterno - r) < tolerance){
                v[i][j] = potencialExterno;
                v[N-i-1][j] = potencialExterno;
                v[i][N-j-1] = potencialExterno;
                v[N-i-1][N-j-1] = potencialExterno;
            }
            else{

                if(fabs(raioInterno - r) < tolerance){
                    v[i][j] = potencialInterno;
                    v[N-i-1][j] = potencialInterno;
                    v[i][N-j-1] = potencialInterno;
                    v[N-i-1][N-j-1] = potencialInterno;
                }
            } 
        }
    }
}

void setAngleCut(double **v, double dx, double dy){
    double x, y, r, ang;

    for(int i = N/2; i < N; i++){
        for(int j = N/2; j < N; j++){
            x = xInicial + i*dx;
            y = yInicial + j*dy;
            r = sqrt(x*x + y*y);
            ang = acos(x/r);

            if(fabs(raioExterno - r) < tolerance && ang < theta){
                v[i][j] = 0;
                v[i][N-j-1] = 0;
            }
            else{
                if(fabs(raioInterno - r) < tolerance && ang < theta){
                    v[i][j] = 0;
                    v[i][N-j-1] = 0;
                }
            }
        }
    }
}

double infinityNorm(double **M, int nL, int nC){

    double norma = 0, soma = 0;

    for(int i = 0; i < nL; i++){
        for(int j = 0; j < nC; j++){
            soma = soma + fabs(M[i][j]);
        }
        if(norma < soma){
            norma = soma;
        }
        soma = 0;
    }

    return norma;
}

void getResults(double **v, double dx, double dy){

    double x, y;
    FILE *arquivo;

    arquivo = fopen("dadosLaplaceOPT.dat", "w");

    fprintf(arquivo, "x\ty\tz\n");

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            x = xInicial + i*dx;
            y = yInicial + j*dy;
            fprintf(arquivo, "%g %g %g\n", x, y, v[i][j]);
        }
    }

    fclose(arquivo);
}

void potentialCalc(double **v, double **v_old, double dx, double dy){
    double x, y, r;

    for(int i = 1; i < N-1; i++){
        for(int j = N/2; j < N-1; j++){
            x = xInicial + i*dx;
            y = yInicial + j*dy;
            r = sqrt(x*x + y*y);
            if(fabs(raioExterno - r) < tolerance && (v[i][j] == potencialExterno )){
                v[i][j] = potencialExterno;
            }
            else{
                if(fabs(raioInterno - r) < tolerance && (v[i][j] == potencialInterno)){
                    v[i][j] = potencialInterno;
                }
                else{
                    v[i][j] = (1.0/4.0)*(v_old[i+1][j] + v_old[i-1][j] + v_old[i][j+1] + v_old[i][j-1]); 
                    v[i][N-j-1] = v[i][j];
                }
            }
        }
    }
}

void finiteDifference(double **v, double **v_old, double dx, double dy){

    double x, y, r;
    long double normaV, normaV_old, normaDif;

    for(int k = 0; k < maxIt; k++){

        for(int a = 0; a < N; a++)
		for(int b = 0; b < N; b++)
			v_old[a][b] = v[a][b];
		
        potentialCalc(v, v_old, dx, dy);

        normaV = infinityNorm(v, N, N);
        normaV_old = infinityNorm(v_old, N, N);
        normaDif = fabs((normaV - normaV_old)/normaV_old);

        if(normaDif < errorTolerance){
            return;
        }
    }
}

int main(int argc, char *argv[]){

    int i, j, k;
    double dx, dy, d, x, y, r;
    double **v, **v_old;

    dx = (xFinal - xInicial)/N;
    dy = (yFinal - yInicial)/N;

    v = malloc(N*sizeof(double *));
    for(int i=0;i<N;i++){
        v[i] = malloc(N*sizeof(double));
    }

    v_old = malloc(N*sizeof(double *));
    for(int i=0;i<N;i++){
        v_old[i] = malloc(N*sizeof(double));
    }

    setContour(v, dx, dy);
    setAngleCut(v, dx, dy);
    finiteDifference(v, v_old, dx, dy);
    getResults(v, dx, dy);

    free(v);
    free(v_old);
}