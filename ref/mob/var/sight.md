## sight var (mob)
**See also:**
+   [invisibility setting (verb)](/ref/verb/set/invisibility.md) 
+   [invisibility var (atom)](/ref/atom/var/invisibility.md) 
+   [see_in_dark var (mob)](/ref/mob/var/see_in_dark.md) 
+   [see_infrared var (mob)](/ref/mob/var/see_infrared.md) 
+   [see_invisible var (mob)](/ref/mob/var/see_invisible.md) 
+   [view proc](/ref/proc/view.md) <!-- -->
**Default value:**
+   0


This controls which objects on the map the mob can see. The
default value of 0 means that the mob can see all objects that are
visible and lit. Different flags in this var can be set to extend or
limit this range. 

The following bit flags are encoded in
mob.sight: 
```
 SEE_INFRA // can see infra-red objects SEE_SELF //
can see self, no matter what SEE_MOBS // can see all mobs, no matter
what SEE_OBJS // can see all objs, no matter what SEE_TURFS // can see
all turfs (and areas), no matter what SEE_PIXELS// if an object is
located on an unlit area, but some of its pixels are // in a lit area
(via pixel_x,y or smooth movement), can see those pixels SEE_THRU // can
see through opaque objects SEE_BLACKNESS // render dark tiles as
blackness BLIND // can\'t see anything 
```

### Example:

```
 usr.sight \|= BLIND // turn on the blind bit usr.sight &=
\~BLIND // turn off the blind bit usr.sight \|=
(SEE_MOBS\|SEE_OBJS\|SEE_TURFS) // turn on several bits at once
usr.sight &= \~(SEE_MOBS\|SEE_OBJS\|SEE_TURFS) // turn off several bits
at once 
```
 

`SEE_PIXELS` draws everything and then
covers hidden turfs with blackness. It is supported in topdown maps
only, not in other map formats. It does not mix well with other flags.
In practice, `SEE_PIXELS` acts as if `SEE_BLACKNESS`, `SEE_TURFS`,
`SEE_OBJS`, and `SEE_MOBS` are all turned on. That is, all atoms are
drawn even on hidden tiles, and black squares are also drawn to cover
them. 

The black tiles rendered by `SEE_BLACKNESS` and
`SEE_PIXELS` are drawn on the default plane 0.