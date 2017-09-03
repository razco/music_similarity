'''
Created on Sep 3, 2017

@author: Raz
'''


def print_mat(mat):
    import sys
    if len(mat.shape) == 2:
        for y in xrange(mat.shape[0]):
            for x in xrange(mat.shape[1]):
                sys.stdout.write('%s\t' % str(mat[y][x]))
            print ''
    else:
        for x in xrange(mat.shape[0]):
            sys.stdout.write('%s   ' % str(list(mat[x])))
        print ''
