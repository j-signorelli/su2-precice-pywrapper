#!/bin/bash


# This auxiliary script simplifies the installation of the preCICE-adapter for SU2. It copies the adapted SU2-files to the correct locations based on the environment variable SU2_HOME.
# Copied from SU2 Adapter
# SU2 version: 7.5.0 "Blackbird"

# SU2 version for which this adapter was made
VERSION="7.5.0 \"Blackbird\""

# Always run this script from current directory
cd "$(dirname "$0")"

# Check for environment variables
printf "\nChecking whether the necessary environment variables are set...\n"
"${SU2_HOME:?You need to set variable SU2_HOME non-empty. Aborting.}"
printf "Necessary environment variables are set.\n"

# Check for SU2 version
printf "\nChecking whether updated Python wrapper and SU2 version are compatible..."
if sed '1,10!d' $SU2_HOME/SU2_CFD/src/SU2_CFD.cpp | grep -Fq "$VERSION"
then
    printf " yes.\n"
else
    printf " no.\nThis wrapper was built using SU2 version $VERSION.\nAborting.\n"
    exit 1;
fi

# Replace SU2 files
printf "Replacing original python wrapper with updated one..."
cp replacement_files/python_wrapper_structure.cpp $SU2_HOME/SU2_CFD/src  || { printf >&2 "\nCannot copy python_wrapper_structure.cpp over. Is variable SU2_HOME set correctly? Are you running the script from the correct directory?\nAborting.\n"; exit 1; }
cp replacement_files/CDriver.hpp $SU2_HOME/SU2_CFD/include/drivers  || { printf >&2 "\nCannot copy CDriver.hpp over. Is variable SU2_HOME set correctly? Are you running the script from the correct directory?\nAborting.\n"; exit 1; }

# Output to guide the user
printf "\nPlease navigate to the SU2 home directory $SU2_HOME and all that you have to do is very simply run:\n"
printf "\n\t\t./ninja -C build install\n\n"

printf "Wrapper successfully copied over. Ideally required added functionalities are implemented in future version of SU2.\n"