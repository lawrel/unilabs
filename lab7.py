import numpy as np
import sys

def diff(char1, char2):
    if ( char1 != char2 ):
        return 1
    else:
        return 0

def find_dists(str1, str2):
    m, n = (len( str1 ) + 1), (len( str2 ) + 1)
    A = np.zeros( shape = (m, n), dtype = np.int )
    B = np.zeros( shape = (m, n), dtype = [("del", 'b'),("sub", 'b'),("ins", 'b')])

    A[:, 0] = range(m)
    A[0, :] = range(n)
    B[:, 0] = (1, 0, 0)
    B[0, :] = (0, 0, 1)

    for i in range(1, m):
        for j in range(1, n):
            dlt = A[(i - 1), j] + 1
            sub = A[(i - 1), (j - 1)] + diff( str1[i - 1], str2[j - 1] )
            ins = A[i, (j - 1)] + 1
            
            min_edit = np.min( [dlt, sub, ins] )

            A[i, j] = min_edit
            B[i, j] = (dlt == min_edit,
                       sub == min_edit,
                       ins == min_edit)

    return A, B

def backtrace(B):
    i, j = (B.shape[0] - 1), (B.shape[1] - 1)
    bt = [(i, j)]

    while (i, j) != (0, 0):
        if ( B[i, j][0] ): 
            i = (i - 1)
        elif ( B[i, j][1] ):   
            i, j = (i - 1), (j - 1)
        else:  
            j = (j - 1)
        bt.append((i, j))

    return bt

def align(str1, str2, bt):
    align1, align2 = [], []
    bt = bt[ :: -1]  

    for k in range(len(bt) - 1):
        i, j = bt[k]
        i1, j1 = bt[(k + 1)]
        
        ch1, ch2 = None, None

        if ( (i1 > i) and (j1 > j) ):   
            ch1 = str1[i]
            ch2 = str2[j]

        elif ( i == i1 ):   
            ch1 = '-'
            ch2 = str2[j]

        else:  
            ch1 = str1[i]
            ch2 = '-'

        align1.append(ch1)
        align2.append(ch2)

    align_str1, align_str2 = "", ""
    for char in align1:
        align_str1 += char
    for char in align2:
        align_str2 += char

    return (''.join([str(x) for x in align1])), (''.join([str(x) for x in align2]))


 
str1, str2 = str( sys.argv[1] ).upper(), str( sys.argv[2] ).upper()
A, B = find_dists( str1, str2 )
bt = backtrace( B )
align_str1, align_str2 = align( str1, str2, bt )

print( "\nEdit Distance: {}".format( A[len(str1)][len(str2)] ) )
print( "\nAlignment:\n{}\n{}".format( align_str1, align_str2 ) )
