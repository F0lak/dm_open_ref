## invisibility var (atom)
**See also:**
*   [invisibility setting (verb)](/ref/verb/set/invisibility.md) -m
*   [opacity var (atom)](/ref/atom/var/opacity.md) -m
*   [see_invisible var (mob)](/ref/mob/var/see_invisible.md) -m
*   [sight var (mob)](/ref/mob/var/sight.md) -m
*   [view proc](/ref/proc/view.md) -m<!-- -->
**Default value:**
*   0
<!-- -->
**Possible values:**
*   0 to 101


This determines the object\'s level of invisibility. The
corresponding mob variable `see_invisible` controls the maximum level of
invisibility that the mob may see. 

A value of 101 is absolutely
invisible, no matter what, and it is filtered from all lists of possible
values for verb arguments. This is intended for objects that exist
purely for some internal purpose, such as \"verb containers\".