[]{#/x, y, and z vars (sound).md}    
## x, y, and z vars (sound)    
**See also:**    
:   [vars (sound)](/sound/var)    
:   [falloff var (sound)](/sound/var/falloff)    
<!-- -->    
**Default value:**    
:   all 0    
Set to different values to give your sound a 3D effect which will be    
applied when it is played. Positive values for `x` will sound as if they    
come from the right, positive `y` sounds like it is above the player\'s    
head, and positive `z` sounds like it is directly ahead. The effect of    
3D sound depends on the player\'s computer\'s sound card, and is greatly    
enhanced when wearing headphones.    
Depending on the value of `falloff`, the settings for the location of    
the sound can also affect its volume. Once the distance passes the value    
of `falloff`, the volume will diminish.    
If these values are all set to 0, you should set `environment` if you    
want to treat it as a 3D sound. Otherwise BYOND will assume this is    
meant to be a non-3D sound such as music or the interface.  