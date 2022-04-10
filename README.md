# inferno tests #
This project is an automation for teats for the coureses  
Intro2cs and Intro2cs2  

the tests will:
1. checks the differences between your output and the school solution output
2. checks the differences between your errors (cerr) and the school solution errors
3. checks for leak memory using valgrind

## how to install ##
1. download tests.py to your computer [from here](https://raw.githubusercontent.com/hodvak/inferno_tests/main/tests.py) (right click and 'save as', save with '.py' extantion)
2. open the linux and make directrory with the following files
   * School solution file with the extantion "sol", must be the only file with "sol" in the name of the file
   * your executable file must be the name of the sol file without the "sol"
   * tests files with "\_test" in the name  
   
   For example, directory the following files:
   * `ex1asol`
   * `ex1a`
   * `ex1a_test00.in`
   * `ex1a_test01.in`
   * `ex1a_test02.in`  
   
   (The directory may also contain the file `ex1a.cc`)
3. move the file `tests.py` to this directory

## how to use ##
1. open the terminal at the directory and wirte the following command:  
   ```bash
   python tests.py
   ```
   For each test the program will print the name of the test and the errors for this test 
   
