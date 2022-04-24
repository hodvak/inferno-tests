# inferno tests #
[![Github licence](https://img.shields.io/github/license/hodvak/inferno_tests)](https://github.com/hodvak/inferno_tests/blob/master/LICENSE)

[![Github release](https://badgen.net/github/release/hodvak/inferno_tests)](https://github.com/hodvak/inferno_tests/releases/latest)
[![Github tag](https://badgen.net/github/tag/hodvak/inferno_tests)](https://github.com/hodvak/inferno_tests/tags/)
[![PyPI version](https://img.shields.io/pypi/v/hac-intro2cs-tests)](https://pypi.org/project/hac-intro2cs-tests/)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This project is an automation for teats for the Hadassah Academic College courses  
Intro2cs and Intro2cs2 

The tests will:
1. Checks the differences between your output and the school solution output
2. Checks the differences between your errors (cerr) and the school solution errors
3. Checks for leak memory using valgrind

## How to Install ##
### Virtual Machine ###
Because the virtual machine has internet connection you may only use the following terminal command
```sh
$ python -m pip install --user hac-intro2cs-tests
``` 
### NoMachine ###
the NoMachine has no internet connection so you must download the file from [PyPI page](https://pypi.org/project/hac-intro2cs-tests/#files)  
Now add the file to the NoMachine and run the following command: 
 command
```sh
$ python -m pip install --user <file_name>
``` 
replace the `<file_name>` with the name of the file you downloaded

## How to Use ##
1. Open the linux (NoMachine or Virtual Machine) and make directory with the following files:
   * School solution file with the extension "sol",  
     must be the only file with "sol" in the name of the file
   * your executable file must be the same name of the the school solution file without the "sol"
   * tests files with "\_test" in the name  
   
   For example, directory with the following files:
   * `ex1asol`
   * `ex1a`
   * `ex1a_test00.in`
   * `ex1a_test01.in`
   * `ex1a_test02.in`  
   
   (The directory may also contain the file `ex1a.cc` for easy use)
   
2. Open the terminal at the directory and write the following command:  
   ```console
   test_ex
   ```
   For each test the program will print the name of the test and the problem in the test (is there output diff, is there errors (cerr) diff, is there a leak memory).  
   
   the tests automatically run with timeout of 5 seconds to your program.  
   to run the program with X seconds timeout, run the following command
   ```console
   test_ex --timeout X
   ```
   To run with no timeout (Strongly recommended not to), set the timeout flag to 0:
   ```console
   test_ex --timeout 0
   ```
   For more information run:
   ```console
   test_ex --help
   ```