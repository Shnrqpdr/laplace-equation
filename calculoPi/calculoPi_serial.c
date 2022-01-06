#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 100000

int main(int argc, char *argv[]){

    struct timespec begin, end;
    FILE *data;

    data = fopen(argv[1], "w+");

    fprintf(data, "PI\tT\n");

	double pi, x_coordinate, y_coordinate, circle_count, realTime, realTimeNano, realTimeSec;
    int step, numberSteps;

    pi = 0.0;
	x_coordinate = 0.0;
	y_coordinate = 0.0;
    circle_count = 0.0;
    numberSteps = N;

    clock_gettime(CLOCK_REALTIME, &begin);

    for (step=0; step<numberSteps; step=step+1){
                            
        x_coordinate=((float)rand())/RAND_MAX;
        y_coordinate=((float)rand())/RAND_MAX;
                
        if(x_coordinate*x_coordinate + y_coordinate*y_coordinate < 1){
            circle_count = circle_count + 1;
        } 
    }

    pi=4.0*circle_count/numberSteps;
    clock_gettime(CLOCK_REALTIME, &end);

    realTimeSec = end.tv_sec - begin.tv_sec;
    realTimeNano = end.tv_nsec - begin.tv_nsec;
	realTime = realTimeSec + realTimeNano*1e-9;

    fprintf(data, "%lf %lf\n", pi, realTime);

    fclose(data);

    return 1;
}