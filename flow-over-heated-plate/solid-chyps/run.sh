#!/bin/sh
set -e -u

# Set the working directory to be the one where this script is located
cd "$(dirname "$0")"

ibrun -n 25 -o 25 chyps_initializer plate.json
ibrun -n 25 -o 25 chyps_heat plate.json