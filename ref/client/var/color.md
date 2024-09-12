## color var (client) 
###### BYOND Version 509



Casts a color multiplication or
[matrix](/ref/%7Bnotes%7D/color-matrix.md)  effect over the entire main map.
This behaves exactly the same as atom.color, and will be combined with
atom.color (which comes first) where present. See
[atom.color](/ref/atom/var/color.md) for more information. 

If a
matrix is used, the alpha column and row will have no effect.


Icons that have the NO_CLIENT_COLOR value in appearance_flags
will not be subject to client.color. This can be useful for HUD objects.


This value can be animated.
### Example:

```
 mob/proc/DayNight(is_day) if(client) client.color = is_day ?
\\ null : \\ list(0.2,0.05,0.05, 0.1,0.3,0.2, 0.1,0.1,0.4) 
```


> [!TIP] 
> **See also:**
> +   [color var (atom)](/ref/atom/var/color.md) 
> +   [appearance_flags var (atom)](/ref/atom/var/appearance_flags.md) 