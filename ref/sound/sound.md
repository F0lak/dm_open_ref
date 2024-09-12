## sound datum
**See also:**
*   [vars (sound)](/ref/sound/var.md) 
*   [sound proc](/ref/proc/sound.md) 
*   [stddef.dm file](/ref/%7B%7Bappendix%7D%7D/stddef%2edm.md) 
*   [load_resource proc](/ref/proc/load_resource.md) 

A `/sound` datum is created by the `sound()` proc or by
`new/sound()`. It can be used to change the way a sound file will play.
When you\'re ready to play the sound, just send it to a player like so:

```
 var/sound/S = sound(\'bubbles.wav\') usr \<\< S 
```



The sound file can be supplied as a list of choices, in which
case the client will play the first compatible sound in the list.