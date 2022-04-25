#!python
import argparse
import os
from subprocess import Popen, PIPE, TimeoutExpired
from typing import Tuple, List

__version__ = "1.3.0"


def test_ex(timeout: int):
    """
    main function to run the tests
    :param timeout: the timeout for each test
    """
    my_files, sol_files, tests_for_all = get_files()
    # make sure all the files exists
    if not sol_files:
        print("Did not find any file with the 'sol' extension (for example 'ex1asol')")
        return

    # make files executable permissions for all users
    for my_file, sol_file, tests in zip(my_files, sol_files, tests_for_all):

        if not my_files:
            print(f"Did not find any file with the name '{sol_file[:-3]}'")
            continue

        if not tests:
            print(
                "There is no test file to run "
                f"(files that start with '{my_file}_test' in the name, for example '{my_file}_test00.in')"
            )
            continue

        run_command(f"chmod a+x {my_file}")
        run_command(f"chmod a+x {sol_file}")

        print("=" * 15 + my_file + "=" * 15)
        for test in tests:
            print("=" * 10 + test + "=" * 10)
            try:
                my_out, my_err = run_command(f"./{my_file} < {test}", timeout=timeout)
            except TimeoutExpired:
                print(
                    "--------TIMEOUT--------\n"
                    f"    Your program cross the timeout limit({timeout} seconds) usually because infinite loop\n"
                    f"    You can run the tests without timeout, or with bigger timeout, using the '-t' flag\n"
                    f"    For more information, use '-h' flag\n"
                )
                continue
            sol_out, sol_err = run_command(f"./{sol_file} < {test}")

            # run the program with valgrind, save only the right line ('in use at exit: ... \n')
            valgrind = run_command(f"valgrind ./{my_file} < {test}")[1]
            valgrind = valgrind[valgrind.index(b"in use at exit: ") :]
            valgrind = valgrind[: valgrind.index(b"\n")]

            if my_out != sol_out:
                my_out = ('"' + repr(my_out)[2:-1] + '"').replace(
                    "\\n", '\\n"\n            "'
                )
                sol_out = ('"' + repr(sol_out)[2:-1] + '"').replace(
                    "\\n", '\\n"\n            "'
                )
                print(
                    "---------OUTPUT--------\n"
                    f'    Outputs not match for "{test}"\n'
                    f"        yours:\n"
                    f"            {my_out}\n"
                    f"        \n"
                    f"        school solution:\n"
                    f"            {sol_out}\n"
                )

            if my_err != sol_err:
                my_err = ('"' + repr(my_err)[2:-1] + '"').replace(
                    "\\n", '\\n"\n            "'
                )
                sol_err = ('"' + repr(sol_err)[2:-1] + '"').replace(
                    "\\n", '\\n"\n            "'
                )
                print(
                    "---------ERROR---------\n"
                    f'    Errors not match for "{test}"\n'
                    f"        yours:\n"
                    f"            {my_err}\n"
                    f"        \n"
                    f"        school solution:\n"
                    f"            {sol_err}\n"
                )

            if b"in use at exit: 0 bytes in 0 blocks" not in valgrind:
                print(
                    "------MEMORY LEAK------\n"
                    f"    Memory leak in {test}:\n"
                    f'        "{valgrind.decode()}"\n'
                )


def get_files() -> Tuple[List[str], List[str], List[List[str]]]:
    """
    get the names of the files for tests
    :return: (the school solution,
              the executable to test,
              the tests inputs names in order)
    """
    files = os.listdir()

    tests = [f for f in files if "_test" in f]
    tests.sort()

    sol_files = [f for f in files if f.endswith("sol")]
    my_files = [
        sol_file[:-3] if sol_file[:-3] in files else "" for sol_file in sol_files
    ]
    if len(sol_files) == 1:
        return my_files, sol_files, [tests]
    return (
        my_files,
        sol_files,
        [
            [test for test in tests if test.startswith(f"{my_file}_test")]
            for my_file in my_files
        ],
    )


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
