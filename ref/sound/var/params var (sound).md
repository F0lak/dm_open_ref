[]{#/sound/var/params}    
## params var (sound) {#params-var-sound byondver="515"}    
**See also:**    
:   [vars (sound)](/ref/sound/var.md)    
<!-- -->    
**Default value:**    
:   null    
Used to set client skin information related to this sound. This can be    
set to an [associative list](/ref/list/associations.md) or a parameter string    
such as you would get from [list2params()](/ref/proc/list2params.md){.code}.    
These are the parameters currently defined:    
on-end    
:   Plays when the sound ends or is stopped.    
on-preempt    
:   Plays when the sound is preempted by another sound. If this isn\'t    
    present, `on-end` still applies if the sound is preempted.    
### Example:    
mob/proc/PlayIntro() var/sound/S = sound(\'intro.ogg\') S.params =    
list(\"on-end\" = \".intro-ended\") src \<\< S mob/verb/\_Intro_Ended()    
set name = \".intro-ended\" src \<\< \"The intro has concluded.\"  