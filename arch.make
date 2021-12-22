# 
# Copyright (C) 1996-2016	The SIESTA group
#  This file is distributed under the terms of the
#  GNU General Public License: see COPYING in the top directory
#  or http://www.gnu.org/copyleft/gpl.txt.
# See Docs/Contributors.txt for a list of contributors.
#
SIESTA_ARCH=intel-mkl
#
# Intel fortran compiler for linux with mkl optimized blas and lapack
#
# Be sure to experiment with different optimization options.
# You have quite a number of combinations to try...
#
FC=ifort 
#
FFLAGS=-w -mp1 -zero -xHOST -fast=2 -O3
FFLAGS_DEBUG= 
LDFLAGS= 
COMP_LIBS=
RANLIB=echo
#
NETCDF_LIBS=
NETCDF_INTERFACE=
FPPFLAGS_CDF=
#
MPI_INTERFACE=
MPI_INCLUDE=
FPPFLAGS_MPI=
#
# GUIDE=/opt/intel/mkl/lib/32/libguide.a
# LAPACK=/opt/intel/mkl/lib/32/libmkl_lapack.a
# BLAS=/opt/intel/mkl/lib/32/libmkl_p3.a
#G2C=/usr/lib/gcc-lib/i386-redhat-linux/2.96/libg2c.a

MKLROOT=/scratch/opt/intel/mkl

LIBS= -Wl,--start-group ${MKLROOT}/lib/intel64/libmkl_intel_lp64.a ${MKLROOT}/lib/intel64/libmkl_sequential.a ${MKLROOT}/lib/intel64/libmkl_core.a -Wl, --end-group -lpthread -lm -ldl

# LIBS=$(LAPACK) $(BLAS) $(G2C) $(GUIDE)  -lpthread 
SYS=bsd
FPPFLAGS= $(FPPFLAGS_CDF) $(FPPFLAGS_MPI)
#
.F.o:
	$(FC) -c $(FFLAGS) $(INCFLAGS)  $(FPPFLAGS) $<
.f.o:
	$(FC) -c $(FFLAGS) $(INCFLAGS)   $<
.F90.o:
	$(FC) -c $(FFLAGS) $(INCFLAGS)  $(FPPFLAGS) $<
.f90.o:
	$(FC) -c $(FFLAGS) $(INCFLAGS)   $<
#







