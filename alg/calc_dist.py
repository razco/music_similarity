'''
Created on May 8, 2017

@author: Raz
'''

import numpy as np
import getopt
import sys
import os


def init_levenshtein_mat(notes1, notes2):
    levenshtein_mat = np.zeros((len(notes1)+1, len(notes2)+1))
    levenshtein_mat[0, :] = np.arange(0, len(notes2)+1)
    levenshtein_mat[:, 0] = np.arange(0, len(notes1)+1)
    return levenshtein_mat


def shift_notes(notes, shift):
    import copy
    notes = copy.deepcopy(notes)
    for curr_notes_idx in xrange(len(notes)):
        curr_notes = np.array(list(notes[curr_notes_idx]))
        curr_notes += shift
        notes[curr_notes_idx] = set(curr_notes)
    return notes


def run(notes1, notes2):
    num_diff_notes = 12
    scores = []
    for shift in xrange(num_diff_notes):
        print 'running shift%d:' % shift
        notes1_shift = shift_notes(notes1, shift)
        levenshtein_mat = run_levenshtein(notes1_shift, notes2)
        score = levenshtein_mat[
            levenshtein_mat.shape[0] - 1, levenshtein_mat.shape[1] - 1]
        print 'score: %f' % score
        scores.append(score)
    print 'running window...'
    max_score_shift = np.argmin(np.array(scores))
    notes1_shift = shift_notes(notes1, max_score_shift)
    run_window_levenshtein(notes1_shift, notes2)


def calc_new_distance(left_ld, top_ld, diag_ld, music_1_val, music_2_val):
    new_cost = np.inf
    # dividing the len of the intersection by the maximum of the
    # melodies length and checking it's larger than 0.5
    # is essential for applying the single notes behavior on chords:
    # we don't want to allow a match of 2 adjacent chords in melody i
    # to the same chord on melody j
    max_num_notes = max(len(music_1_val), len(music_2_val))
    if 1.0 * len(music_1_val.intersection(music_2_val)) / max_num_notes > 0.5:
        new_cost = 0.0
    new_dist = np.min(np.array([left_ld + 1, top_ld + 1, diag_ld + new_cost]))
    return new_dist


def run_window_levenshtein(music_1, music_2):
    window_size = 10
    assert len(music_1) >= 10 and len(music_2) >= 10
    max_score = window_size * 999.0
    max_score_music_1_idx = -1
    max_score_music_2_idx = -1
    for music_1_win_idx in xrange(0, len(music_1) - window_size + 1):
        rel_music_1 = music_1[music_1_win_idx:music_1_win_idx + window_size]
        for music_2_win_idx in xrange(0, len(music_2) - window_size + 1):
            rel_music_2 = music_2[music_2_win_idx:music_2_win_idx + window_size]
            levenshtein_mat = run_levenshtein(rel_music_1, rel_music_2)
            score = levenshtein_mat[len(rel_music_1), len(rel_music_2)]
            if score < max_score:
                max_score = score
                max_score_music_1_idx = music_1_win_idx
                max_score_music_2_idx = music_2_win_idx
    print (
        'best match with window: %f at music1 index %d, and music2 index %d' %
        (max_score, max_score_music_1_idx, max_score_music_2_idx)
    )


def run_levenshtein(music_1, music_2):
    levenshtein_mat = init_levenshtein_mat(music_1, music_2)
    for music_1_idx in range(len(music_1)):
        lm_1_idx = music_1_idx + 1  # levenshtein_mat idx for music 1
        for music_2_idx in range(len(music_2)):
            lm_2_idx = music_2_idx + 1  # levenshtein_mat idx for music 2
            new_dist = calc_new_distance(
                levenshtein_mat[lm_1_idx, lm_2_idx - 1],
                levenshtein_mat[lm_1_idx - 1, lm_2_idx],
                levenshtein_mat[lm_1_idx - 1, lm_2_idx - 1],
                music_1[music_1_idx], music_2[music_2_idx]
            )
            levenshtein_mat[lm_1_idx, lm_2_idx] = new_dist
    return levenshtein_mat


def extract_notes(midi_file):
    import midi.midifile_to_notes as to_notes
    return to_notes.extract_notes(midi_file)


def load_args():
    script_name = os.path.basename(sys.argv[0])
    midi_file1 = ''
    midi_file2 = ''
    argv = sys.argv[1:]
    try:
        opts, _ = getopt.getopt(argv, "h1:2:", ["midi1=", "midi2="])
    except getopt.GetoptError:
        print '%s -1 <midi_file1> -2 <midi_file2>' % script_name
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print '%s -1 <midi_file1> -2 <midi_file2>' % script_name
            sys.exit()
        elif opt in ("-1", "--midi1"):
            midi_file1 = arg
        elif opt in ("-2", "--midi2"):
            midi_file2 = arg
    if midi_file1 == '' or midi_file2 == '':
        print '%s -1 <midi_file1> -2 <midi_file2>' % script_name
        sys.exit()
    return midi_file1, midi_file2


def main():
    midi_file1, midi_file2 = load_args()
    notes1 = extract_notes(midi_file1)
    notes2 = extract_notes(midi_file2)
    run(notes1, notes2)


if __name__ == '__main__':
    main()
