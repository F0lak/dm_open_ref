[]{#/sound/var/frequency}    
## frequency var (sound)    
**See also:**    
:   [vars (sound)](ref/sound/var)    
:   [pitch var (sound)](ref/sound/var/pitch)    
<!-- -->    
**Default value:**    
:   0    
Any value from -100 to 100 will play this sound at a multiple of its    
normal frequency. Set to 2 to play at double speed, for example, or -1    
to play backwards. A value of 0 or 1 will play the sound at its normal    
frequency.    
Set to a specific frequency (in Hz) outside of the -100 to 100 range to    
change the playback rate of the sound. A negative value is also allowed.    
The value 0 means that the sound should be played as-is. This value will    
take effect when the sound is sent to a player.    
CD-quality sound is sampled at 44.1 KHz, which is a value of 44100.    
Other common sample rates for .wav files are 8000, 11025, and 22050.    
(11025 is usually a good quality for most sound effects without making    
file size too large.) If you know the file\'s sample rate, doubling the    
value will play it at a higher pitch and twice as fast; halving it will    
play it at a lower pitch and twice as slow.    
To make a sound play at a different speed but keep its pitch intact, set    
`frequency` to the speed multiple you want (e.g., 1.2 for 20% faster)    
and set `pitch` to the inverse (e.g., 1/1.2).  