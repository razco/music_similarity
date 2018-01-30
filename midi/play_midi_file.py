'''
Created on May 20, 2017

@author: Raz
'''

import numpy as np
import pygame
import pygame.midi
pygame.init()
pygame.midi.init()

# playing music!

# pygame.mixer.music.load('midi_files/felix_jaehn_aint_nobody.mid')

# pygame.mixer.music.load('midi_files/MIDI from felix_jaehn_aint_nobody.mid.mid')
# pygame.mixer.music.load('midi_files/MIDI from felix_jaehn_aint_nobody.mid_step_0_get_tracks_notes.mid')
# pygame.mixer.music.load('midi_files/MIDI from felix_jaehn_aint_nobody.mid_step_1_mod_tracks_notes.mid')
# pygame.mixer.music.load('midi_files/MIDI from felix_jaehn_aint_nobody.mid_step_2_remove_low_volume_tracks_notes.mid')
# pygame.mixer.music.load('midi_files/MIDI from felix_jaehn_aint_nobody.mid_step_3_remove_dups_of_tracks_notes.mid')
# pygame.mixer.music.load('midi_files/MIDI from felix_jaehn_aint_nobody.mid_step_4_remove_successive_same_chords_in_tracks.mid')




# pygame.mixer.music.load('part_melody_Frere Jacques.mid')
pygame.mixer.music.load('part_melody_Mahler Symphony No.1 Mov.3.mid')
# pygame.mixer.music.load('part_melody_the carpenters - please mr postman.mid')
# pygame.mixer.music.load('part_melody_portugal the man - feel it still.mid')
# pygame.mixer.music.load('part_melody_chaka_khan_aint_nobody.mid')
# pygame.mixer.music.load('part_melody_felix_jaehn_aint_nobody.mid')
# pygame.mixer.music.load('midi_files/chaka_khan_aint_nobody.mid')
# pygame.mixer.music.load('midi_files/Feels - pharrel williams.mid')
# pygame.mixer.music.load('midi_files/Sugababes - Shape_clean.mid')
# pygame.mixer.music.load('part_melody_Feels - pharrel williams.mid')
# pygame.mixer.music.load('midi_files/sting - shape of my heart_clean.mid')
# pygame.mixer.music.load('midi_files/Sugababes - Shape.mid')
# pygame.mixer.music.load('gagagaga_no_low_vol_dups.mid')
# pygame.mixer.music.load('part_melody_Sugababes - Shape.mid')
# pygame.mixer.music.load('part_melody_Feels - pharrel williams.mid')
# pygame.mixer.music.load('part_melody_sting - shape of my heart.mid')
# pygame.mixer.music.load('midi_files/Chaka Kahn - Ain\'t Nobody.mid')
# pygame.mixer.music.load('midi_files/MIDI from chaka_khan_aint_nobody.mid.mid')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    print pygame.mixer.music.get_pos()
    pygame.time.wait(1000)

# # loading music for reading!
# # list all the midi devices
# for x in range( 0, pygame.midi.get_count() ):
#     print pygame.midi.get_device_info(x)

# # open a specific midi device
# inp = pygame.midi.Input(1,0)
# a = inp.read()
# print a

print 'gaga'