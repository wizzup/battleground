import subprocess as sp
from select import select

def stdin_ready(p, timeout=0.1):
    fn = p.stdin.fileno()

    r, w, x = select([]
            ,[fn]
            ,[]
            , timeout)
    return w == [fn]

def out_ready(out, timeout):
    fn = out.fileno()

    r, w, x = select([fn]
            ,[]
            ,[]
            , timeout)
    return r == [fn]

def stdout_ready(p, timeout=0.1):
    return out_ready(p.stdout, timeout)

def stderr_ready(p, timeout=0.1):
    return out_ready(p.stderr, timeout)

def print_ready(p):
    print("i %s, o %s, e %s" % (stdin_ready(p), stdout_ready(p), stderr_ready(p)))

def main():
    p0 = sp.Popen(["python", "-u", "bot0.py"]
        , stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE
        , universal_newlines=True)

    # do read/write for initial value
    init = 4 
    init_in = str(init) + "\n"
    
    if stdin_ready(p0):
        wi = p0.stdin.write(init_in)
        p0.stdin.flush()

    if stdout_ready(p0):
        outs = p0.stdout.readline()
        print("out: %s" % outs)

    if stderr_ready(p0):
        errs = p0.stderr.readline()
        print("err: %s" % errs)

    for i in range(init):
        i_in = str(i) + "\n"

        if stdin_ready(p0):
            wi = p0.stdin.write(i_in)
            p0.stdin.flush()

        if stdout_ready(p0):
            outs = p0.stdout.readline()
            print("out: %s" % outs)

        if stderr_ready(p0):
            errs = p0.stderr.readline()
            print("err: %s" % errs)

__main__ = main()

def test_nop():
    assert 0 == 0
