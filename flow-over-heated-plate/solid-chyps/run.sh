#!usr/bin/bash
set -e -u

# Set the working directory to be the one where this script is located
cd "$(dirname "$0")"

chyps_initializer plate.json
chyps_heat plate.json