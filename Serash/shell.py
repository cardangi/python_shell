import sys, shlex, os

SHELL_STATUS_RUN = 1
SHELL_STATUS_STOP = 0

def main():
    print ("Users command:")
    print ("-G = edit here")
    print ("-L = edit here")
    print ("-O = edit here")

try:
    if sys.argv[1] == "-G":
        ### EDIT HERE ###
    if sys.argv[1] == "-L":
        ### EDIT HERE ###
    if sys.argv[1] == "-O":
        ### EDIT HERE ###
except IndexError:
    main()
    
#Splitting the user's command
#(mkdir "my folder") will return a list ['mkdir', '"my folder"]
try:
    def tokenize(string):
        return shlex.split(string)

    def execute(cmd_tokens):
        pid = os.fork()

        if pid == 0:
            os.execvp(cmd_tokens[0], cmd_tokens)
        elif pid > 0:
            while True:
                wpid, status = os.waitpid(pid, 0)

                if os.WIFEXITED(status) or os.WIFSIGNALED(status):
                    break

        return SHELL_STATUS_RUN

    def shell_loop():
        status = SHELL_STATUS_RUN

        while status == SHELL_STATUS_RUN:
            sys.stdout.write('> ')
            sys.stdout.flush()

            cmd = sys.stdin.readline()

            cmd_tokens = tokenize(cmd)

            status = execute(cmd_tokens)

    def main():
        shell_loop()

    if __name__ == "__main__":
        main()
except:
    ### Trash collection / crash prevention. If it crash, you copy the except and put here^ ###
