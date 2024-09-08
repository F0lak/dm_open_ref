[]{#/proc/flick}
## flick proc
**See also:**
:   [icon_state var (atom)](#/atom/var/icon_state)
<!-- -->
**Format:**
:   flick(Icon,Object)
<!-- -->
**Args:**
:   Icon: An icon file or state name.
:   Object: The target object.
Cause the icon attached to Object to be temporarily replaced with the
specified icon or icon state for the duration of the animation. This is
a purely visual effect and does not effect the actual value of the
object\'s icon variable.
### Example:
flick(\'blink.dmi\',usr) //show another icon flick(\"fight\",usr) //show
usr\'s fight state
The target object may be any atom or image.