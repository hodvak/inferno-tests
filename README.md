# Inferno Tests #
[![Github licence](https://img.shields.io/github/license/hodvak/inferno_tests)](https://github.com/hodvak/inferno_tests/blob/master/LICENSE)

[![Github release](https://badgen.net/github/release/hodvak/inferno_tests)](https://github.com/hodvak/inferno_tests/releases/latest)
[![Github tag](https://badgen.net/github/tag/hodvak/inferno_tests)](https://github.com/hodvak/inferno_tests/tags/)
[![PyPI version](https://img.shields.io/pypi/v/hac-intro2cs-tests)](https://pypi.org/project/hac-intro2cs-tests/)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This project is an automation for teats for the Hadassah Academic College courses  
Intro2cs and Intro2cs2.

The tests will:
1. Check the differences between your output and the school solution output.
2. Check the differences between your errors (cerr) and the school solution errors.
3. Check for leak memory using `valgrind`.

## How to Install ##
### Virtual Machine ###
Because the virtual machine has internet connection you may only use the following terminal command:
```sh
$ python -m pip install --user hac-intro2cs-tests
``` 
### NoMachine ###
The NoMachine has no internet connection so you must download the package 
file from [PyPI page](https://pypi.org/project/hac-intro2cs-tests/#files) (the `.whl` file is recommended).  
Now add the file to the NoMachine and run the following command:
```sh
$ python -m pip install --user <file_name>
``` 
Replace the `<file_name>` with the name of the file you downloaded

## How to Use ##
1. Open the linux (NoMachine or Virtual Machine) and make directory with the following files:
   * School solution file, must be with the extension "sol",  
     must be the only file with "sol" in the name of the file.
   * Your executable file, must be the same name as the school solution file without the "sol".
   * Tests files, must contain "\_test" in their name.
   
   For example, directory with the following files:
   * `ex1asol`
   * `ex1a`
   * `ex1a_test00.in`
   * `ex1a_test01.in`
   * `ex1a_test02.in`  
   
   (The directory may also contain the file `ex1a.cc` for easy use)
   
2. Open the terminal at the directory and write the following command:  
   ```sh
   $ python -m test_ex
   ```
   For each test the program will print the name of the test and the problem with the test 
   (if there is outputs diff, if there is errors (cerr) diff, if there is a memory leak).  

### Alias ###
You can add [alias](https://www.tecmint.com/create-alias-in-linux/) to the command by writing the next line to the file `~/.tcshrc`:
```sh
alias test_ex python -m test_ex
``` 
You may run the following command to do so:
```sh
$ echo "alias test_ex python -m test_ex" >> ~/.tcshrc
```

Now you can run the command:
```sh
$ test_ex
``` 
Instead of: 
```sh
$ python -m test_ex
``` 

## A Little Bit More ##
The tests automatically run with timeout of 5 seconds to *your* program.  
To change the timeout you may use the `-t` or `--timeout` flag:
To run the program with X seconds timeout, run the following command
```sh
$ python -m test_ex --timeout X
```
To run with no timeout (Strongly recommended not to), set the timeout flag to 0:
```sh
$ python -m test_ex --timeout 0
```
For more information run:
```sh
test_ex --help
```
