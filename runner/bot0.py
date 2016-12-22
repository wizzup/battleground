from sys import stderr

def main():
    init_var = None
    try:
        inp = input()
        init_var = inp
        print("main (cout): " + inp)
        print("main (cerr): %s" % inp, file=stderr)
    except EOFError:
        print("EOF (main)", file=stderr)
        exit(1)

    loop()

def loop():
    loop_var = None
    try:
        inp = input()
        # print("loop (cout): " + inp)
        print("loop (cerr): %s" % inp, file=stderr)
    except EOFError:
        print("EOF (loop)", file=stderr)
        exit(1)

    loop()

__main__ = main()
