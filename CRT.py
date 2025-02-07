'''
python CRT.py [<b-list>] -- [<m-list>]
eg. python CRT.py 1 2 -- 4 5
'''
import sys
from Calcu import Inverse, GCD
from functools import reduce

def CRT(b_arr, m_arr):
    if (b_arr.__len__() != m_arr.__len__()) or (b_arr.__len__() == 0):
        return -1
    M = reduce(lambda x,y : x*y, m_arr)
    M_arr = [M // m for m in m_arr]
    ''' MR means M_inverse '''
    MR_arr = [Inverse(Mi % mi, mi) for Mi, mi in zip(M_arr, m_arr)]
    return sum([b*Mi*MiR for b, Mi, MiR in zip(b_arr, M_arr, MR_arr)]) % M

def main(argv):
    b_arr = []
    m_arr = []
    flag = 'b'
    for arg in argv:
        if arg == "--":
            flag = 'm'
            continue
        if flag == 'b':
            b_arr.append(int(arg))
        if flag == 'm':
            m_arr.append(int(arg))
    else:
        print("x =", CRT(b_arr, m_arr))

if __name__ == "__main__":
    main(sys.argv[1:])