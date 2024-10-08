## sound proc


**Format:**
+   sound(file,repeat=0,wait,channel,volume)
+   [(supports named arguments)]{.small}

**Args:**
+   file: A sound file to play
+   repeat: 1 to play sound repeatedly
+   wait: 0 to interrupt current sound on channel; 1 to wait in queue
+   channel: 0 for any available channel, 1-1024 for specific channel
    (non-MIDI only)
+   volume: 100 for full volume (default), 0 for none, or any value in
    between


This is used to play a sound file. 

The sound file must
be a music or sample file. Music files include MIDI (.mid or .midi), and
module formats .mod, .it, .s3m, .xm, and .oxm. A sample file used for
sound effects can be .wav, .ogg, .raw, .wma, or .aiff.* 

The
following example plays some sound files. Note that `sound()` is not
even necessary when you don\'t need to set any additional parameters.
### Example:

```dm
 usr << \'giggle.wav\' // play a giggle once usr <<
sound(\'gigue.midi\',1) // repeat gigue usr << sound(\'boom.wav\',
volume=50) // play an explosion at half volume 
```



[*See **Notes** under [sound support](/ref/DM/sound.md) for more
information.]{.small}

> [!TIP] 
> **See also:**
> +   [sound datum](/ref/sound.md) 
> +   [vars (sound)](/ref/sound/var.md) 
> +   [<< output operator](/ref/operator/%3c%3c/output.md) 
> +   [load_resource proc](/ref/proc/load_resource.md) 