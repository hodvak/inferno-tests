import os
from subprocess import Popen, PIPE
from typing import Tuple, List

__version__ = "1.0.0"


def main():
    my_file, sol_file, tests = get_files()
    for test in tests:
        print("=" * 10 + test + "=" * 10)
        my_out, my_err = run_command(f"./{my_file} < {test}")
        sol_out, sol_err = run_command(f"./{sol_file} < {test}")

        # run the program with valgrind, save only the right line ('in use at exit: ... \n')
        valgrind = run_command(f"valgrind ./{my_file} < {test}")[1]
        valgrind = valgrind[valgrind.index(b"in use at exit: "):]
        valgrind = valgrind[:valgrind.index(b"\n")]

        if my_out != sol_out:
            print(f"not match output for file '{test}'\nyours:\n{my_out}\nsol:\n{sol_out}")

        if my_err != sol_err:
            print(f"not match errors in file '{test}'\nyours:\n{my_err}\nsol:\n{sol_err}")

        if b"in use at exit: 0 bytes in 0 blocks" not in valgrind:
            print(f"did not free memory in {test}:")
            print(f"    {valgrind.decode()}")


def get_files() -> Tuple[str, str, List[str]]:
    """
    get the names of the files for tests
    :return: (the school solution,
              the executable to test,
              the tests inputs names in order)
    """
    files = os.listdir()
    sol_file = [f for f in files if 'sol' in f][0]
    my_file = sol_file[:-3]
    tests = [f for f in files if '_test' in f]
    tests.sort()
    return my_file, sol_file, tests


def run_command(command: str) -> Tuple[bytes, bytes]:
    """
    run the command and return the output (cout) and the errors (cerr) for given command using bash
    :param command: the command to run
    :return: (output(cout), errors(cerr))
    """
    return Popen(command,
                 shell=True,
                 executable="/bin/bash",
                 stdout=PIPE,
                 stderr=PIPE
                 ).communicate()


if __name__ == '__main__':
    main()
