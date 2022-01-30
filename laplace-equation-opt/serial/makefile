CC=gcc
CFLAGS=-lm
COMPILER_FLAGS=-pg -g

laplace.x: eletric-potential.c
	$(CC) eletric-potential.c -o laplace.x $(CFLAGS)

.PHONY: clean

clean:
	rm -fr *.x *.o *.dat *.png *~ core
