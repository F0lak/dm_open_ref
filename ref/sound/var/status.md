## status var (sound)
**See also:**
*   [vars (sound)](/ref/sound/var.md) 
*   [SoundQuery proc (client)](/ref/client/proc/SoundQuery.md) <!-- -->
**Default value:**
*   0


Alter the way the sound is heard by affecting several different
on/off values which combine as bit flags. 
```
 SOUND_MUTE // do
not play the sound SOUND_PAUSED // pause sound SOUND_STREAM // create as
a stream SOUND_UPDATE // update a playing sound 
```
 

Use
the `|` operator to combine these values. The setting you choose will
take effect when the sound is sent to a player.


`SOUND_MUTE | SOUND_UPDATE` will mute a sound, but it will
continue to play. It can be unmuted while still playing by resending it
with `status=SOUND_UPDATE`. 

`SOUND_PAUSED | SOUND_UPDATE` will
pause a sound. It can be restarted from its current position by
resending it with `status=SOUND_UPDATE`. 

`SOUND_STREAM` will
create this sound as a stream. Streams take less memory, but can not
play multiple times at once, nor can they play in reverse. This flag is
only valid the first time that a sound is played in a particular mode
(normal vs. 3D). Changing the flag later will not change the stream
status of the sound in that mode. 

`SOUND_UPDATE` updates the
settings for the sound currently playing on the specified channel. If
this flag is not set or no channel is specified, the sound will start
again from the beginning. 

Some of the flags for this value may
be filled in by the `SoundQuery` proc.