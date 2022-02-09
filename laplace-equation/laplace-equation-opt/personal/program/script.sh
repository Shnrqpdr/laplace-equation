#!/bin/bash

for i in $(seq 1 8)
do
	{ time ./laplace.x $i ; } 2> tempo_thread_$i.txt
done


