import sys
import json
# import pprint
import mido
import numpy as np

def remove_duplicates(notes_for_alg):
    # run until the second note: because of comparison with the previous one
    for idx in xrange(len(notes_for_alg)-1, 0, -1):
        if len(notes_for_alg[idx]) == 0:
            del notes_for_alg[idx]
            continue
        curr_num_notes = len(notes_for_alg[idx])
        if curr_num_notes != len(notes_for_alg[idx - 1]):
            continue
        if all([notes_for_alg[idx][note_idx] == notes_for_alg[idx - 1][note_idx] for note_idx in xrange(curr_num_notes)]):
            del notes_for_alg[idx]
    return notes_for_alg
            

def midifile_to_dict(mid):
    tracks = []
    for track in mid.tracks:
        tracks.append([vars(msg).copy() for msg in track])

    return {
        'ticks_per_beat': mid.ticks_per_beat,
        'tracks': tracks,
    }

# mid = mido.MidiFile(sys.argv[1])
mid = mido.MidiFile('AUD_DW0146.mid')

mid_dict = midifile_to_dict(mid)
track_data = np.array(mid_dict['tracks'][0])
notes_data = track_data[np.flatnonzero(np.array(['note' in mid_dict['tracks'][0][idx] for idx in xrange(len(track_data))]))]
lyrics_data = track_data[np.flatnonzero(np.array(['text' in mid_dict['tracks'][0][idx] for idx in xrange(len(track_data))]))]

notes_for_alg = []
notes_for_alg.append([])
NUM_DIFFERENT_NOTES = 12
for note in notes_data:
    if note['time'] > 0:
        is_last_note_empty = len(notes_for_alg[-1]) == 0
        if not is_last_note_empty:
            notes_for_alg[-1] = np.unique(np.array(notes_for_alg[-1]))
            notes_for_alg.append([])
    if note['velocity'] > 0:
        notes_for_alg[-1].append(note['note'] % 12)
# print(json.dumps(midifile_to_dict(mid), indent=2))
notes_for_alg = remove_duplicates(notes_for_alg)
print notes_for_alg
with open('AUD_DW0146.json', 'w') as f:
    json.dump(mid_dict, f)


