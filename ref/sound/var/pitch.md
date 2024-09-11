## pitch var (sound) 
###### BYOND Version 515
**See also:**
*   [vars (sound)](/ref/sound/var.md) -m
*   [frequency var (sound)](/ref/sound/var/frequency.md) -m<!-- -->
**Default value:**
*   0


Can be used to shift the pitch of a sound up or down. This
works similarly to frequency except that it doesn\'t impact playback
speed. 

The value of this var should be a multiple relative to
1, so for instance to go up a full octave, the value would be 2; to go
down an octave, use 0.5. 

Note* The filter that handles pitch
shifting only goes from 0.5 to 2. The player will stack up to three
filters if it has to, so the range is really from 0.125 to 8. You will
however hear much poorer quality at more extreme values. 

To
make a sound play at a different speed but keep its pitch intact, set
`frequency` to the speed multiple you want (e.g., 1.2 for 20% faster)
and set `pitch` to the inverse (e.g., 1/1.2).
### Example:

```
 client var/sound/music // music currently playing
proc/PlayMusic(music) music = new(music) music.channel = 100 src \<\<
music proc/UpTempo(amount = 0.1) // 10% faster if(!music) return
music.frequency = (music.frequency \|\| 1) + amount music.pitch = 1 /
music.frequency music.status \|= SOUND_UPDATE src \<\< music 
```
