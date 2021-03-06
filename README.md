# Inferno Tests #
[![Github licence](https://img.shields.io/github/license/hodvak/inferno-tests)](https://github.com/hodvak/inferno-tests/blob/master/LICENSE)

[![Github release](https://badgen.net/github/release/hodvak/inferno-tests)](https://github.com/hodvak/inferno-tests/releases/latest)
[![Github tag](https://badgen.net/github/tag/hodvak/inferno-tests)](https://github.com/hodvak/inferno-tests/tags/)
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
python -m pip install --user hac-intro2cs-tests
``` 
### NoMachine ###
The NoMachine has no internet connection so you must download the package 
file from [PyPI page](https://pypi.org/project/hac-intro2cs-tests/#files) (the `.whl` file is recommended).  
Now add the file to the NoMachine and run the following command:
```sh
python -m pip install --user <file_name>
``` 
Replace the `<file_name>` with the name of the file you downloaded

## How to Use ##
1. Open the linux (NoMachine or Virtual Machine) and make directory with the following files:
   * School solution files, must be with the extension "sol",  
   * Your executable file, must be the same name as the school solution files names without the "sol".
   * Tests files, must contain "\_test" in their name.
     if there are more then 1 sol file, the file must start with the executable file name following by "\_test"
   
   For example, directory with the following files:
   * `ex1asol`
   * `ex1a`
   * `ex1a.cc` (optional)
   * `ex1a_test00.in`
   * `ex1a_test01.in`
   * `ex1a_test02.in` 
   * `ex1asol`
   * `ex1b`
   * `ex1b.cc` (optional)
   * `ex1b_test00.in`
   * `ex1b_test01.in`
   * `ex1b_test02.in` 
   
   
2. Open the terminal at the directory and write the following command:  
   ```sh
   python -m test_ex
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
touch ~/.tcshrc
echo "alias test_ex python -m test_ex" >> ~/.tcshrc
```

Now you can run the command:
```sh
test_ex
``` 
Instead of: 
```sh
python -m test_ex
``` 

## A Little Bit More ##
### Timeout ##
The tests automatically run with timeout of 5 seconds to *your* program.  
To change the timeout you may use the `-t` or `--timeout` flag:  
To run the program with X seconds timeout, run the following command
```sh
test_ex --timeout X
```
To run with no timeout (Strongly recommended not to), set the timeout flag to 0:
```sh
test_ex --timeout 0
```
### Specific Test ###
If you want to test specific test you may use the `-s` or `--specific` in the following way

test all tests for ex1a:
```sh
test_ex --specific ex1a
``` 
test specific tests for ex1a (`ex1a_test01.in`):
```sh
test_ex --specific ex1a_test01.in
``` 
### More ###
For more information run:
```sh
test_ex --help
```
