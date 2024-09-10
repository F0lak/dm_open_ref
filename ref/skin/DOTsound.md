[]{#/DOTsound (client command).md}/commands/.sound}    
## .sound (client command) {#sound-client-command byondver="516"}    
**See also:**    
:   [sound proc](/proc/sound)    
:   [sound datum](/sound)    
:   [client commands](/%7Bskin%7D/commands)    
<!-- -->    
**Format:**    
:   .sound *file* *options*    
:   .sound none *options*    
Plays, stops, or modifies a sound. This command can be used for instance    
to play a click sound when using mouse macros, for instance, without    
waiting for the server to initiate the sound which would introduce a    
small delay.    
    .sound 'click.ogg'    
The file can be `none` or `-` when updating or stopping a sound. Any    
options should be separated by spaces; most are in a `name=value`    
format, as seen below.    
Supported options are:    
update    
:   This action is updating a channel rather than playing a new sound.    
    It corresponds to the [SOUND_UPDATE](/sound/var/status){.code}    
    status flag.    
channel=*N*    
:   Specifies a channel.    
volume=*N*    
:   Sets the volume.    
mute\    
mute=*T*    
:   Mutes the sound; the `update` option is implied.    
pause\    
pause=*T*    
:   Pauses the sound; the `update` option is implied.    
wait    
:   The new sound will queue up in the specified channel, and play after    
    the current sound is done.    
repeat\    
repeat=*T*\    
repeat=once/infinite/rewind    
:   Specifies whether, and how, the sound repeats.    
\**T* represents a true/false value. True values include `true`, `on`,    
or 1. False would be `false`, `off`, or 0.  