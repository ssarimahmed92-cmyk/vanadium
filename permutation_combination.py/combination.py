import main_file as mf
import factorial
def com():
    global a
    global b
    a = factorial.fact(mf.n)
    b = factorial.fact(mf.n-mf.r)
    c = factorial.fact(mf.r)
    nCr = a/(c*b)
    return nCr
