[]{#/sound/var/file}    
## file var (sound)    
**See also:**    
:   [sound proc](/ref/proc/sound.md)    
:   [vars (sound)](/ref/sound/var.md)    
:   [SoundQuery proc (client)](/ref/client/proc/SoundQuery.md)    
This is the file that will be played when the sound is sent to a player.    
If this value is a list of files rather than a single file, the client    
will play the first compatible sound in the list. This can be useful for    
developing webclient games, where .ogg is preferred by most browsers for    
audio, but .mp3 is needed for others.    
This var may be filled in by the `SoundQuery` proc.  