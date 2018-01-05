'''
Created on Sep 3, 2017

@author: Raz
'''
import numpy as np
import sys
from collections import namedtuple


def print_mat(mat):
    if len(mat.shape) == 2:
        for y in xrange(mat.shape[0]):
            for x in xrange(mat.shape[1]):
                sys.stdout.write('%s\t' % str(mat[y][x]))
            print ''
    else:
        for x in xrange(mat.shape[0]):
            sys.stdout.write('%s   ' % str(list(mat[x])))
        print ''


def shift_notes(num_diff_notes, notes, shift):
    import copy
    notes = copy.deepcopy(notes)
    for curr_notes_idx in xrange(len(notes)):
        curr_notes = np.array(list(notes[curr_notes_idx]))
        curr_notes += shift
        curr_notes %= num_diff_notes
        notes[curr_notes_idx] = set(curr_notes)
    return notes


def print_notes(notes):
    for chord_idx, chord in enumerate(notes):
        sys.stdout.write('%s\t' % str(chord))
        if chord_idx % 5 == 0:
            # new line
            print ''


def print_final_result(res):
    v_res = namedtuple("v_res", ["v", "track1", "ch1", "track2", "ch2"])
    v_results = []
    for a1, a2 in res.iteritems():
        for b1, b2 in a2.iteritems():
            for c1, c2 in b2.iteritems():
                for d1, d2 in c2.iteritems():
                    v_results.append(v_res(v=(d2.lp - d2.ep), track1=a1, ch1=b1, track2=c1, ch2=d1))
#                     print a1, b1, c1, d1, 'start: ', d2.melody1_start, d2.melody2_start, 'len: ', d2.melody1_len, d2.melody2_len, 'lp: ', d2.lp, 'ep: ', d2.ep, 'v: ', d2.lp - d2.ep

    # sort by v before displaying
    v_results.sort(key=lambda x: x.v, reverse=True)
    for v_result in v_results:
        track1 = v_result.track1
        ch1 = v_result.ch1
        track2 = v_result.track2
        ch2 = v_result.ch2
        curr_res = res[track1][ch1][track2][ch2]
        print track1, ch1, track2, ch2, 'start: ', curr_res.melody1_start, curr_res.melody2_start, 'len: ', curr_res.melody1_len, curr_res.melody2_len, 'lp: ', curr_res.lp, 'ep: ', curr_res.ep, 'v: ', curr_res.lp - curr_res.ep, 'success %: ', int(100*(1.0 - 1.0* curr_res.ep/curr_res.lp) + 0.5) if curr_res.lp > 0 else 0


def ratio(arr, val):
    '''
    return: ratio of val inside the list arr
    '''
    arr = np.array(arr)
    return float(np.sum(arr == val))/float(len(arr))
