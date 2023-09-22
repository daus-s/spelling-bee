import os
import sys
import subprocess
from os.path import exists






def main():
    args = sys.argv[1:]
    file_exists = exists("./a.out")
    if not file_exists:
        os.system("g++ main.cc")

    cmd=f'./a.out {args[0]} {args[1]} 1'
    result = subprocess.check_output(cmd, shell=True)
    print(result[:-2])


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()