CC=gcc
CFLAGS=-lm

laplace.x: eletric-potential.o
	$(CC) -o laplace.x eletric-potential.o $(CFLAGS)

.PHONY: clean

clean:
	rm -fr *.x *.o *.dat *.png *~ core
