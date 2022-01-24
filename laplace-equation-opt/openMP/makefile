CC=gcc
CFLAGS=-lm
COMPILER_FLAGS=-O2 -fexpensive-optimizations -m64 -foptimize-register-move -funroll-loops -ffast-math -mtune=native -march=native -fopenmp

laplace.x: eletric-potential.c
	$(CC) $(COMPILER_FLAGS) eletric-potential.c -o laplace.x $(CFLAGS)

.PHONY: clean

clean:
	rm -fr *.x *.o *.dat *.png *~ core
