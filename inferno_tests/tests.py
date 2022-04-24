import argparse
import os
from subprocess import Popen, PIPE, TimeoutExpired
from typing import Tuple, List

__version__ = "1.2.1"


def test_ex(timeout: int):
    my_file, sol_file, tests = get_files()

    # make sure all the files exists
    if not sol_file:
        print("Did not find any file with the 'sol' extension (for example 'ex1asol')")
        return
    if not my_file:
        print(f"Did not find any file with the name '{sol_file[:-3]}'")
        return
    if not tests:
        print(
            "There is no test file to run (files with '_test' in the name, for example 'ex1a_test00.in')"
        )
        return

    # make files executable permissions for all users
    run_command(f"chmod a+x {my_file}")
    run_command(f"chmod a+x {sol_file}")

    for test in tests:
        print("=" * 10 + test + "=" * 10)
        try:
            my_out, my_err = run_command(f"./{my_file} < {test}", timeout=timeout)
        except TimeoutExpired:
            print(
                f"Your program cross the timeout limit({timeout} seconds) usually because infinite loop\n"
                f"You can run the tests without timeout, or with bigger timeout, using the '-t' flag\n"
                f"For more information, use '-h' flag"
            )
            continue
        sol_out, sol_err = run_command(f"./{sol_file} < {test}")

        # run the program with valgrind, save only the right line ('in use at exit: ... \n')
        valgrind = run_command(f"valgrind ./{my_file} < {test}")[1]
        valgrind = valgrind[valgrind.index(b"in use at exit: ") :]
        valgrind = valgrind[: valgrind.index(b"\n")]

        if my_out != sol_out:
            print(f'Outputs not match for "{test}"\nyours:\n{my_out}\nsol:\n{sol_out}')

        if my_err != sol_err:
            print(f'Errors not match for  "{test}"\nyours:\n{my_err}\nsol:\n{sol_err}')

        if b"in use at exit: 0 bytes in 0 blocks" not in valgrind:
            print(f"Memory leak in {test}:")
            print(f'    "{valgrind.decode()}"')


def get_files() -> Tuple[str, str, List[str]]:
    """
    get the names of the files for tests
    :return: (the school solution,
              the executable to test,
              the tests inputs names in order)
    """
    files = os.listdir()

    tests = [f for f in files if "_test" in f]
    tests.sort()

    sol_file = [f for f in files if f.endswith("sol")]
    if len(sol_file) == 0:
        return "", "", tests
    sol_file = sol_file[0]

    my_file = sol_file[:-3]
    if my_file not in files:
        return "", sol_file, tests

    return my_file, sol_file, tests


def run_command(command: str, timeout: int = None) -> Tuple[bytes, bytes]:
    """
    run the command and return the output (cout) and the errors (cerr) for given command using bash
    :param command: the command to run
    :param timeout: timeout for the command None for no timeout
    :return: (output(cout), errors(cerr))
    """
    return Popen(
        command, shell=True, executable="/bin/bash", stdout=PIPE, stderr=PIPE
    ).communicate(timeout=timeout)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version", "-v", action="version", version=f"Inferno Tests {__version__}"
    )
    parser.add_argument(
        "--timeout",
        "-t",
        help="set the timeout to your program or 0 for no timeout, default value is 5",
        type=int,
        default=5,
    )
    args = parser.parse_args()
    test_ex(args.timeout if args.timeout != 0 else None)


if __name__ == "__main__":
    main()
