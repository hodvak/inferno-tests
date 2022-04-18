# inferno tests #
[![Github release](https://badgen.net/github/release/hodvak/inferno_tests)](https://github.com/hodvak/inferno_tests/releases/latest)
[![Github tag](https://badgen.net/github/tag/hodvak/inferno_tests)](https://github.com/hodvak/inferno_tests/tags/)
[![Github licence](https://img.shields.io/github/license/hodvak/inferno_tests)](https://github.com/hodvak/inferno_tests/blob/master/LICENSE)

This project is an automation for teats for the courses  
Intro2cs and Intro2cs2  

The tests will:
1. Checks the differences between your output and the school solution output
2. Checks the differences between your errors (cerr) and the school solution errors
3. Checks for leak memory using valgrind

## How to Install ##
1. Download the code [from here](https://github.com/hodvak/inferno_tests/archive/refs/heads/main.zip).  
   Or by selecting the wanted stable version [from here](https://github.com/hodvak/inferno_tests/releases/) and download the `inferno_tests.zip` zip file
2. Move the zip file to your linux (virtual machine/inferno)
3. Open the zip file and extract the `inferno_tests` directory to wherever you want 
   (strongly recommended not to save it on the desktop (for clear desktop)) 
4. Open the terminal at `inferno_tests` directory and run the following command:
   ```console
   ./install.sh
   ```

## How to Update ##
If there are any update you may download the version you want and just replace the old `tests.py` with the new `tests.py`

## How to Use ##
1. Open the linux and make directory with the following files:
   * School solution file with the extension "sol",  
     must be the only file with "sol" in the name of the file
   * your executable file must be the same name of the the school solution file without the "sol"
   * tests files with "\_test" in the name  
   
   For example, directory the following files:
   * `ex1asol`
   * `ex1a`
   * `ex1a_test00.in`
   * `ex1a_test01.in`
   * `ex1a_test02.in`  
   
   (The directory may also contain the file `ex1a.cc`)
   
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