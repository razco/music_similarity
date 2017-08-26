'''
Created on Aug 26, 2017

@author: Raz
'''
import mido
import numpy as np


def midifile_to_dict(mid):
    tracks = []
    for track in mid.tracks:
        tracks.append([vars(msg).copy() for msg in track])

    return {
        'ticks_per_beat': mid.ticks_per_beat,
        'tracks': tracks,
    }


aaa = mido.MidiFile('AUD_DW0146.mid')
aaa.tracks
print 'buya'

mid_dict = midifile_to_dict(aaa)
track_data = np.array(mid_dict['tracks'][0])
notes_inds = np.flatnonzero(np.array(['note' in mid_dict['tracks'][0][idx] for idx in xrange(len(track_data))]))
notes_data = track_data[notes_inds]

outfile = mido.MidiFile()
track = mido.MidiTrack()
outfile.tracks.append(track)

notes_inds_to_keep = np.array(range(10, 50, 1))  # inds in the levenshtein mat that are similar
orig_notes_inds_to_keep = set(notes_inds[notes_inds_to_keep])

for idx in xrange(len(track_data) - 1, -1, -1):
    msg = aaa.tracks[0][idx]
    if 'note' in msg.type and idx not in orig_notes_inds_to_keep:
        aaa.tracks[0].pop(idx)

aaa.save('part_melody.mid')

