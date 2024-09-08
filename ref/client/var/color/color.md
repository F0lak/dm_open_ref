[]{#/client/var/color}
## color var (client) {#color-var-client byondver="509"}
**See also:**
:   [color var (atom)](#/atom/var/color)
:   [appearance_flags var (atom)](#/atom/var/appearance_flags)
Casts a color multiplication or [matrix](#/%7Bnotes%7D/color-matrix)
effect over the entire main map. This behaves exactly the same as
atom.color, and will be combined with atom.color (which comes first)
where present. See [atom.color](#/atom/var/color) for more information.
If a matrix is used, the alpha column and row will have no effect.
Icons that have the NO_CLIENT_COLOR value in appearance_flags will not
be subject to client.color. This can be useful for HUD objects.
This value can be animated.
### Example:
mob/proc/DayNight(is_day) if(client) client.color = is_day ? \\ null :
\\ list(0.2,0.05,0.05, 0.1,0.3,0.2, 0.1,0.1,0.4)