import os, sys, re

while (True):
    cmd = input(f'{os.getcwd()} $ ').split()
    if len(cmd) == 0:
        continue
    # exit
    elif len(cmd) == 1 and cmd[0] == "exit":
        print("\tExiting; bye bye")
        sys.exit(0)
    # Change directory
    elif cmd[0] == "cd":
        if len(cmd) == 2:
            try:
                os.chdir(cmd[1])
            except FileNotFoundError:
                print(f'\tNo such directory {cmd[1]}')
            continue
        print("\tCD only takes one directory")
    # execute a command
    else:
        print("\tchild FORKED..")
        child = os.fork()
        if (child < 0):
            os.write(2, ("fork fail %d\n" % child).enconde())
            sys.exit(1)
        elif (child == 0):
            for dir in re.split(":", os.environ['PATH']):
                program = "%s/%s" % (dir, cmd[0])
                try:
                    os.execve(program, cmd, os.environ)
                except FileNotFoundError:
                    pass
            os.write(2, ("Could not execute line %s\n" % cmd[0]).encode())
            sys.exit(1)
        else:
            os.wait()

            os.write(1, ("\tIM THE PARENT HERE\n").encode())