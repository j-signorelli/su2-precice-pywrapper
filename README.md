# SU2 Python Wrapper Adapter

The SU2 adapter now leverages the SU2 Python wrapper and preCICE Python bindings to couple SU2 using preCICE in a minimally invasive way. This adapter simply updates existing and implements new functions in the SU2 Python wrapper allowing for simple preCICE implementation with implicit coupling. This adapter currently works for SU2 versions 7.5.0 and 7.5.1 "Blackbird". Both conjugate heat-transfer and fluid-structure interaction can be completed with this adapter.

## Contents
<!-- toc orderedList:0 -->

- [Contents](#contents)
- [Building the Adapter](#building-the-adapter)
    - [SU2](#su2)
    - [preCICE](#precice)
    - [Adapter](#adapter)
- [Running Simulations](#running-simulations)
    - [SU2 Configuration File](#su2-configuration-file)
    - [Running SU2 w/ preCICE](#running-su2-w/-precice)

<!-- tocstop -->
## Building the Adapter
### SU2
Download SU2 v7.5.1 "Blackbird" from directly from https://github.com/su2code/SU2/releases/tag/v7.5.1. Note that both swig and mpi4py must be installed to use the SU2 Python wrapper. After installing the adapter, the flag `-Denable-pywrapper=true` must be specified.

### preCICE
In addition to having successfully installed preCICE, the preCICE Python bindings must also be installed. For installing preCICE, please navigate to https://precice.org/installation-overview.html. After successfully installing preCICE, please follow the instructions at https://precice.org/installation-bindings-python.html to get the preCICE Python bindings. As a test, run the following command:

        python3 -c "import precice"

If there are no errors, then preCICE and its Python bindings were successfully installed.

### Adapter
In order to couple SU2 using preCICE, *python_wrapper_structure.cpp* and *CDriver.hpp* must be updated. This adapter provides the updated files. The shell script *installUpdatedWrapper*, which comes with this adapter, automatically replaces the files in your SU2 directory with these updated files and provides the correct commands to re-configure and re-install SU2 with the added adjustments. For this to work, the `SU2_HOME` variable must be set to your SU2 directory prior to running.

SU2 will advise you to add this variable (and others) to your ~/.bashrc (Linux) or ~/.bash_profile (Mac) after configuring, so it may already be set if SU2 is already configured and installed on your computer. To install the adapter, run from the adapter directory:

        ./installUpdatedWrapper

The script will not execute if the environment variable `SU2_HOME` is not set or empty.

If you do not want to use this script, manually copy the files to the locations given in it. The environment variable needs to be defined as stated above, nevertheless.

After copying the adapter files to the correct locations within the SU2 package, SU2 can be configured and built just like the original version of the solver suite. Please refer to the installation instructions provided with the SU2 source code. SU2 should be built with MPI support in order to make use of parallel functionalities and must be built with pywrapper functionality enabled. The script *installUpdatedWrapper* states recommended command sequences for both the configuration and the building process upon completion of the execution.

## Running Simulations