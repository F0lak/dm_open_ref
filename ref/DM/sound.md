## sounds
**See also:**
*   [FILE_DIR definition](/ref/DM/preprocessor/define/FILE_DIR.md) 
*   [cache](/ref/DM/cache.md) 
*   [sound proc](/ref/proc/sound.md) 
*   [/sound datum](/ref/sound.md) 
*   [load_resource proc](/ref/proc/load_resource.md) 

A sound stored in a file may be referenced by putting single
quotes around the filename. The file extension determines the type of
sound. Currently supported music types include MIDI (.mid or .midi), and
module formats .mod, .it, .s3m, .xm, and .oxm. Supported sound effect
formats include .wav, .ogg, .mp3, .raw, .wma, and .aiff.
### Example:

```
 world \<\< sound(\'fugue.midi\') 
```
 

This
example plays the specified midi file to all players.