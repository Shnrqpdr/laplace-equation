void finiteDifference(double **v, double **v_old, double dx, double dy, int chunk, int numberThreads){
    
    int a, b, i, j, k;
    double x, y, r;

    omp_set_num_threads(numberThreads);

    #pragma omp parallel private(a, b, x, y, r, i, j, k) shared(v, v_old)
    {
        for(k = 0; k < maxIt; k++){

            for(a = 0; a < N; a++)
            for(b = 0; b < N; b++)
                v_old[a][b] = v[a][b];

            #pragma omp for schedule(dynamic, chunk) collapse(2)
            for(i = 1; i < N-1; i++){
                for(j = N/2; j < N-1; j++){

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
    }
}