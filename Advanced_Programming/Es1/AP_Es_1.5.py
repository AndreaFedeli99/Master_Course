# Similarly to the ls-l example please implement:

# 1. The cat command, i.e., a command that given a list of files prints their content on the terminal (man cat to get more info).
# 2. The chmod command, i.e., a command that permits to change the access mode of a given group of files (man chmod to get more info)
# 3. The more command, i.e., a command that given a file prints its content 30 rows at a time and wait a keystroke every 30 rows before printing the next 30.

import sys, os

def cat(file_names):
    for i in range(len(file_names)):
        print(open(file_names[i]).read())

def chmod(file_names, mode):
    os.chmod(file_names, int(mode, base=8))

def more(file_name):
    with open(file_name) as f:
        content = f.read().split("\n")
    
    lines_number = len(content)
    lines_read = 0
    while (lines_number - lines_read) > 0:
        print(*content[lines_read:lines_read+30], sep="\n")
        input("Press a key to read the next 30 lines...")
        lines_read += 30 if lines_number - lines_read > 30 else lines_number - lines_read

if __name__ == "__main__":
    cat(sys.argv[1:])
    chmod(sys.argv[1:], "0o700")
    more(sys.argv[1])