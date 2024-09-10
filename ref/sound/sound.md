[]{#/sound datum.md}    
## sound datum.md datum    
**See also:**    
:   [vars (sound datum.md)]/sound datum.md/var    
:   [sound datum.md proc]/proc/sound datum.md    
:   [stddef.dm file]/%7B%7Bappendix%7D%7D/stddef%2edm    
:   [load_resource proc]/proc/load_resource    
A `/sound datum.md` datum is created by the `sound datum.md()` proc or by `new/sound datum.md()`.    
It can be used to change the way a sound datum.md file will play. When you\'re    
ready to play the sound datum.md, just send it to a player like so: var/sound datum.md/S =    
sound datum.md(\'bubbles.wav\') usr \<\< S    
The sound datum.md file can be supplied as a list of choices, in which case the    
client will play the first compatible sound datum.md in the list.  