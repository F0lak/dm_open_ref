## turn proc (applied to an icon)

**Format:**
+   turn(Icon, Angle)
<!-- -->
**Returns:**
+   The rotated icon.
<!-- -->
**Args:**
+   Icon: an icon to rotate
+   Angle: An angle in degrees (clockwise rotation).
### Example:

```
 mob/verb/drink() //this effect is very confusing! usr.icon =
turn(usr.icon,90) usr \<\< \"Woah! That stuff is powerful!\" sleep(200)
usr.icon = turn(usr.icon,-90) 
```
 

An icon that is not
square will not be turned. 

If the icon is an /icon datum, a new
datum will be created as the result.

**See also:**
+   [turn proc](/ref/proc/turn.md) 
+   [icon](/ref/icon.md) <!-- -->