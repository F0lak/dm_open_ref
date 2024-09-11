## params var (sound) 
###### BYOND Version 515
**See also:**
*   [vars (sound)](/sound/var)
<!-- -->
**Default value:**
*   null


Used to set client skin information related to this sound. This
can be set to an [associative list](/list/associations) or a parameter
string such as you would get from
[`list2params()`](/proc/list2params). 

These are the
parameters currently defined:
on-end
*   Plays when the sound ends or is stopped.
on-preempt
*   Plays when the sound is preempted by another sound. If this isn\'t
    present, `on-end` still applies if the sound is preempted.
### Example:

```
 mob/proc/PlayIntro() var/sound/S = sound(\'intro.ogg\')
S.params = list(\"on-end\" = \".intro-ended\") src \<\< S
mob/verb/\_Intro_Ended() set name = \".intro-ended\" src \<\< \"The
intro has concluded.\" 
```
