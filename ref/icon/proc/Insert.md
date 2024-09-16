## Insert proc (icon)

<!-- -->
**Format:**
+   Insert(new_icon,icon_state,dir,frame,moving,delay)
+   [(supports [named arguments](/ref/proc/arguments/named.md) ]{.small}
<!-- -->
**Args:**
+   new_icon: an icon file or /icon object to insert
+   icon_state: an optional text string, specifying a single icon state
    to change or add to this icon
+   dir: an optional direction; the inserted icon will only be added for
    this direction
+   frame: an optional animation frame (starting at 1); the inserted
    icon will only be added for this frame
+   moving: Non-zero to insert as a movement state, 0 for a regular
    non-movement state
+   delay: 0 or null to leave unchanged; positive to set delay for a
    frame and turn rewind off; negative to set delay and rewind


This adds additional states or images to an existing icon,
allowing you to build directional, animated, and multi-state icons on
the fly. If the state you wish to insert already exists in the file, it
will be altered; otherwise it will be added. An animation may be built a
piece at a time, for example by inserting an icon into the NORTH
direction for animation frame 3.
### Example:

``` dm
 // start with a non-animated arrow icon var/icon/I =
new(\'arrow.dmi\') // make a new state called \"blink\" var/icon/J =
new(\'arrow.dmi\') I.Insert(J, \"blink\", delay=-1) // set rewind flag
// create darker shades of the arrow var/n = 2 for(var/light=9,
light\>=5, light\--) J = new(\'arrow.dmi\') J.SetIntensity(light/10)
I.Insert(J, \"blink\", frame=n++) // congratulations, you have a
pulsating arrow icon = I 
```
 

The icon resulting from
this example has two states: The original arrow, and a new state called
\"blink\" that pulsates between full and ½ luminance. To use the
blinking state after that, set the atom\'s icon_state to \"blink\".


(Note for animations: When building an animated icon_state from
scratch, you can only add 16 new animation frames at a time; i.e.,
frame\<=total_frames+16. Higher values for frame will be ignored. This
is a safety precaution.) 

If you insert an icon of a different
size, the src icon will be resized to match the size of new_icon. (The
only exception is if you are using the TILED_ICON_MAP map_format, and
new_icon is a single tile being inserted as a chunk into a larger icon.
If icon_state, such as \"2,0\" or \"open 0,0\", already exists in src as
one of its smaller pieces, then new_icon will be inserted in its place.)


When inserting an individual animation frame, you can change
the delay for just that frame only. If you don\'t specify a delay, the
nearest frame\'s delay will be used. If this is the first frame being
inserted into an icon, then the delay will default to 1 tick. Remember,
if your delay is positive, it will turn off the rewind flag for that
entire icon state; negative will turn it on.

> [!TIP] 
> **See also:**
> +   [procs (icon)](/ref/icon/proc.md) 
> +   [New proc](/ref/icon/proc/New.md) 
> +   [map_format var (world)](/ref/world/var/map_format.md) 
> +   [Big icons](/ref/notes/big-icons.md) 
> +   [Tiled icons](/ref/notes/tiled-icons.md) 