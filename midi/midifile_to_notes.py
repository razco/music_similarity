'''
Created on Aug 26, 2017

@author: Raz
'''
# import pprint
import mido
import numpy as np


def remove_duplicates(notes_for_alg, notes_for_alg_inds):

    # modify melody: remove common preceding notes
    prev_notes = notes_for_alg[0]
    for idx in xrange(len(notes_for_alg) - 1):
        curr_notes = notes_for_alg[idx + 1]
        notes_for_alg[idx + 1] = curr_notes.difference(prev_notes)
        prev_notes = curr_notes

    # run until the second note: because of comparison with the previous one
    for idx in xrange(len(notes_for_alg) - 1, 0, -1):
        if len(notes_for_alg[idx]) == 0:
            del notes_for_alg[idx]
            del notes_for_alg_inds[idx]
            continue
        curr_num_notes = len(notes_for_alg[idx])
        if curr_num_notes != len(notes_for_alg[idx - 1]):
            continue
        if len(notes_for_alg[idx].symmetric_difference(
                notes_for_alg[idx - 1])) == 0:
            del notes_for_alg[idx]
            del notes_for_alg_inds[idx]

#     for idx in xrange(len(notes_for_alg)):
#         notes_for_alg[idx] = np.array(list(notes_for_alg[idx]))

    return notes_for_alg, notes_for_alg_inds


def midifile_to_dict(mid):
    tracks = []
    for track in mid.tracks:
        tracks.append([vars(msg).copy() for msg in track])

    return {
        'ticks_per_beat': mid.ticks_per_beat,
        'tracks': tracks,
    }


def extract_notes(midi_file, debug=False):
    import pickle
    mid = mido.MidiFile(midi_file)

    mid_dict = midifile_to_dict(mid)
    track_data = np.array(mid_dict['tracks'][0])
    notes_inds = np.flatnonzero(np.array(['note' in mid_dict[
        'tracks'][0][idx] for idx in xrange(len(track_data))]))
    notes_data = track_data[notes_inds]
    text_inds = np.flatnonzero(np.array(['text' in mid_dict[
        'tracks'][0][idx] for idx in xrange(len(track_data))]))
    text_data = track_data[text_inds]
    lyrics_data_inner_inds = np.flatnonzero(np.array([lyrics_data_curr[
        'type'] == 'lyrics' for lyrics_data_curr in text_data]))
    lyrics_data = text_data[lyrics_data_inner_inds]
    lyrics_data_inds = text_inds[lyrics_data_inner_inds]

    notes_for_alg = []
    notes_for_alg.append(set())
    notes_for_alg_inds = []
    notes_for_alg_inds.append(notes_inds[0])
    NUM_DIFFERENT_NOTES = 12
    for note_idx, note in enumerate(notes_data):
        if note['time'] > 0:
            is_last_note_empty = len(notes_for_alg[-1]) == 0
            if not is_last_note_empty:
                notes_for_alg.append(set())
                notes_for_alg_inds.append(notes_inds[note_idx])
        if note['velocity'] > 0:
            notes_for_alg[-1].add(note['note'] % NUM_DIFFERENT_NOTES)

    # print(json.dumps(midifile_to_dict(mid), indent=2))
    if debug:
        pickle.dump(notes_for_alg, open(
            'debug_output/orig_%s.pickle' % midi_file.split('/')[-1], 'wb'))
    notes_for_alg, notes_for_alg_inds = remove_duplicates(
        notes_for_alg, notes_for_alg_inds)
    return notes_for_alg, notes_for_alg_inds
