#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 100000

int main(int argc, char *argv[]){

    struct timespec begin, end;
    FILE *data;

    data = fopen(argv[1], "w+");

    fprintf(data, "NT\tPI\tCH\tT\n");

	double pi, x_coordinate, y_coordinate, circle_count, realTime, realTimeSec, realTimeNano;
	int step, chunk, numberSteps, numberThreads, tid, n;
	
    pi = 0.0;
	x_coordinate = 0.0;
	y_coordinate = 0.0;
    circle_count = 0.0;

	numberSteps = N;
    tid = -1;
    srand(time(NULL));
    
    for(chunk = 1; chunk <= 10001; chunk+=100){

    	numberThreads = 8;

    	while(numberThreads != 0){

       		circle_count = 0.0;
       		omp_set_num_threads(numberThreads);
		
            clock_gettime(CLOCK_REALTIME,&begin);
            #pragma omp parallel private(step, x_coordinate, y_coordinate, tid)
            {
                    #pragma omp for reduction(+:circle_count) schedule(dynamic, chunk) 
                        
                    for (step=0; step<numberSteps; step=step+1){  
                        x_coordinate=((float)rand())/RAND_MAX;
                        y_coordinate=((float)rand())/RAND_MAX;
                    
                        if(x_coordinate*x_coordinate + y_coordinate*y_coordinate < 1){
                            circle_count = circle_count + 1;
                    } 
                }
            }

            pi=4.0*circle_count/numberSteps;

   			clock_gettime(CLOCK_REALTIME, &end);

            realTimeSec = end.tv_sec - begin.tv_sec;
            realTimeNano = end.tv_nsec - begin.tv_nsec;
			realTime = realTimeSec + realTimeNano*1e-9;

    		fprintf(data, "%d %lf %d %lf\n", numberThreads, pi, chunk, realTime);
   			numberThreads--;

   		}
   	}

   	fclose(data);

    return 1;
}
