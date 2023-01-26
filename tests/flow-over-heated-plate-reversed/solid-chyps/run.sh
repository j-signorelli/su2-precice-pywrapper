#!/bin/sh
set -e -u

# Set the working directory to be the one where this script is located
cd "$(dirname "$0")"

# CHyPS must first be initialized separately -- use same MPI partitions: chyps_initializer plate.json
chyps_heat plate.json