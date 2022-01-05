CC=gcc
CFLAGS=-lm
COMPILER_FLAGS=-pg -g

laplace.x: eletric-potential.o
	$(CC) $(COMPILER_FLAGS) -o laplace.x eletric-potential.o $(CFLAGS)

.PHONY: clean

clean:
	rm -fr *.x *.o *.dat *.png *~ core
