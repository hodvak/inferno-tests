# inferno tests #
This project is an automation for teats for the coureses  
Intro2cs and Intro2cs2  

the tests will:
1. checks the differences between your output and the school solution output
2. checks the differences between your errors (cerr) and the school solution errors
3. checks for leak memory using valgrind

## How to Install ##
1. download `tests.py` to your computer [from here](https://raw.githubusercontent.com/hodvak/inferno_tests/main/inferno_tests/tests.py) (right click and 'save as', save as 'tests.py')
2. download `install.sh` to your computer [from here](https://raw.githubusercontent.com/hodvak/inferno_tests/main/inferno_tests/install.sh) (right click and 'save as', save as 'install.sh')
3. open your Inferno and save both files in the same directory (It is recommended not to save on the desktop (for cleaner desktop))
4. open terminal in the directory and run the following command:
   ```console
   ./install.sh
   ```

## How to Update ##
if there are any update on the `tests.py` file, you may only download the new `tests.py` to your computer [from here](https://raw.githubusercontent.com/hodvak/inferno_tests/main/inferno_tests/tests.py) (right click and 'save as', save as 'tests.py')
and replace it with the old one

## How to Use ##
1. open the linux and make directory with the following files
   * School solution file with the extension "sol", must be the only file with "sol" in the name of the file
   * your executable file must be the name of the sol file without the "sol"
   * tests files with "\_test" in the name  
   
   For example, directory the following files:
   * `ex1asol`
   * `ex1a`
   * `ex1a_test00.in`
   * `ex1a_test01.in`
   * `ex1a_test02.in`  
   
   (The directory may also contain the file `ex1a.cc`)
   
2. open the terminal at the directory and write the following command:  
   ```console
   test_ex
   ```
   For each test the program will print the name of the test and the errors for this test 