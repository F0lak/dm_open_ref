
## icon (proc)

**Format:**
+   turn(Icon, Angle)

**Arguments:**
+   Icon: an icon to rotate
+   Angle: An angle in degrees (clockwise rotation).

**Returns:**
+   The rotated icon.
***

```dm

mob/verb/drink()
   //this effect is very confusing!
   usr.icon = turn(usr.icon,90)
   usr << "Woah!  That stuff is powerful!"
   sleep(200)
   usr.icon = turn(usr.icon,-90)

```


An icon that is not square will not be turned.

If the icon is an /icon datum, a new datum will be created as the result.
***
**Related Pages:**
+    [turn proc](/ref/proc/turn)
+    [icon](/ref/icon)
