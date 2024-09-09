[]{#/sound/var/wait}    
## wait var (sound)    
**See also:**    
:   [sound proc](/ref/proc/sound.md)    
:   [vars (sound)](/ref/sound/var.md)    
:   [SoundQuery proc (client)](/ref/client/proc/SoundQuery.md)    
<!-- -->    
**Default value:**    
:   0 (do not wait)    
Set to 1 to wait for other sounds in this channel to finish before    
playing this one.    
The `SoundQuery` proc fills in this value with the total duration of    
sounds that are queued to be played on this channel.  