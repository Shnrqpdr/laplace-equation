#!/bin/bash
#########################################################################

        #Author: PEDRO HENRIQUE DOS SANTOS CUNHA
        #Date: 27/11/2021

#########################################################################

        # KNOW INFO. CHANGE THOSE ACCORDINGLY WHAT YOU WILL USE

header=104 # rows number of the header
footer=3   # rows number of the footer
grid=240*240*240 #size of grid
columnsNumber=6 #number of columns
let matrixBegin=$header+1

######################################################################## 

        # CREATING THE FILES WITH ONLY THE MATRIX

tail -n "+$matrixBegin" "device.xsf" >> device.dat
tail -n "+$matrixBegin" "devmol.xsf" >> devmol.dat
tail -n "+$matrixBegin" "molecule.xsf" >> molecule.dat

########################################################################

        # OPERATING MATRIXES

paste molecule.dat device.dat | awk -v n=$columnsNumber '{for (i=1; i<=n; i++) printf "%s%s", ($i + $(i+n)), (i==n)?ORS:OFS}' >> sumMatrix.dat
paste devmol.dat sumMatrix.dat | awk -v n=$columnsNumber '{for (i=1; i<=n; i++) printf "%s%s", ($i - $(i+n)), (i==n)?ORS:OFS}' >> operatedMatrix.dat
head -n $header devmol.xsf >> finalMatrix.xsf
cat operatedMatrix.dat >> finalMatrix.xsf
tail -n $footer devmol.xsf >> finalMatrix.xsf

#########################################################################

        # REMOVING AUXILIAR FILES 

rm *.dat 


