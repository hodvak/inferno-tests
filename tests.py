import os
from subprocess import Popen, PIPE

files = os.listdir()
sol_file = [f for f in files if 'sol' in f][0]
my_file = sol_file[:-3]
tests = [f for f in files if '_test' in f]
tests.sort()
for test in tests:
    my_out,err1 = Popen(f"./{my_file} < {test}", shell=True,executable="/bin/bash",stdout=PIPE,stderr=PIPE).communicate()
    sol_out,err2 = Popen(f"./{sol_file} < {test}", shell=True,executable="/bin/bash",stdout=PIPE,stderr=PIPE).communicate()
    _,valgrind = Popen(f"valgrind ./{my_file} < {test}", shell=True,executable="/bin/bash",stdout=PIPE,stderr=PIPE).communicate()
    print("-"*10 +test+ "-"*10+'\n')
    if my_out != sol_out:
        print (f"error for file {test} yours:\n{my_out}\nsol:\n{sol_out}")
    
    if err1 != err2:
        print (f"error for errors in file {test} yours:\n{err1}\nsol:\n{err2}")
        
    if not b"in use at exit: 0 bytes in 0 blocks" in valgrind:
        print (f"did not free memory in {test}")
