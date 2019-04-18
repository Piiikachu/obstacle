#!/bin/bash
#SBATCH -p paratera
#SBATCH -N 10
#SBATCH -n 240

source /PARA/app/scripts/cn-module.sh
module load sparta/mpi3-intel18/22Jun18
yhrun spa_mpi<in.obs

