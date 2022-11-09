# -*- coding: utf8 -*-
import numpy as np
from synthesizer import Player, Synthesizer, Waveform
import time

#canco = "Bartomeu_El_Portugues"
canco = "Desembarca_Jordi"

#################################################

player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
song = str("/home/propietario/Documents/Personal/Python_scripts/"+canco+".csv") #Nom cançó
vel = 1.55 #Velocitat de reproducció

musictime = np.loadtxt(song, dtype=float, delimiter=',', usecols=0, skiprows=1)
freq = np.loadtxt(song, dtype=float, delimiter=',', usecols=1, skiprows=1)

start_time = time.time()


musictime = musictime/vel


timing = np.zeros(len(musictime))


print("\n Now tuning: %s \n" % canco)
#Càlcul de temps que ha de durar cada nota
for i in range(len(musictime)):
	if i==0:
		timing[i] = 0
	else:
		timing[i] = musictime[i]-musictime[i-1]


#Reproducció cançó
for i in range(len(freq)):
	player.play_wave(synthesizer.generate_constant_wave(freq[i], timing[i]))
