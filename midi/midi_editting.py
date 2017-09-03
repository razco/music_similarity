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


def test():
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


def run(midi_file, midi_notes_inds, midi_series_len, midi_start_note):
    orig_note_ind_to_keep_start = midi_notes_inds[midi_start_note]
    orig_note_ind_to_keep_end = (
        midi_notes_inds[midi_start_note + midi_series_len])

#     rel_notes_inds = (
#         midi_notes_inds[midi_start_note:midi_start_note + midi_series_len])

    aaa = mido.MidiFile(midi_file)
    for idx in xrange(len(aaa.tracks[0]) - 1, -1, -1):
        msg = aaa.tracks[0][idx]
        if 'note' in msg.type and (
            idx < orig_note_ind_to_keep_start or
            idx >= orig_note_ind_to_keep_end
        ):
            #  if 'note' in msg.type and idx not in rel_notes_inds:
            aaa.tracks[0].pop(idx)

    aaa.save('part_melody_%s' % midi_file.split('/')[-1])

# running shift0:
# score: 561.000000
# running shift1:
# score: 719.000000
# running shift2:
# score: 707.000000
# running shift3:
# score: 691.000000
# running shift4:
# score: 749.000000
# running shift5:
# score: 671.000000
# running shift6:
# score: 805.000000
# running shift7:
# score: 731.000000
# running shift8:
# score: 763.000000
# running shift9:
# score: 789.000000
# running shift10:
# score: 789.000000
# running shift11:
# score: 849.000000
# running window...
# best match with window: 38.000000 at music1 index 98, and music2 index 393


def main():
    import midifile_to_notes

    midi_file1 = 'midi_files/sting - shape of my heart.mid'
    _, midi_notes_inds1 = midifile_to_notes.extract_notes(midi_file1)
    midi_series_len1 = 12
    midi_start_note1 = 9
    run(midi_file1, midi_notes_inds1, midi_series_len1, midi_start_note1)

    midi_file2 = 'midi_files/Sugababes - Shape.mid'
    _, midi_notes_inds2 = midifile_to_notes.extract_notes(midi_file2)
    midi_series_len2 = 12
    midi_start_note2 = 7
    run(midi_file2, midi_notes_inds2, midi_series_len2, midi_start_note2)


if __name__ == '__main__':
    main()
