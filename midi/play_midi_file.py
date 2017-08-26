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
pygame.mixer.music.load("part_melody.mid")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
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