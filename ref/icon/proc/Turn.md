
## Turn (proc)

**Format:**
+   Turn(angle)

**Arguments:**
+   angle: an angle in degrees
***
This rotates the icon clockwise by the specified amount.


```dm

mob/verb/drink()
   //this effect is very confusing!
   var/icon/I = new(usr.icon)
   I.Turn(90)
   usr.icon = I
   usr << "You feel a little tipsy!"

   sleep(200)

   I.Turn(-90)  //turn it back
   usr.icon = I //should have just saved original value

```


If an icon is not square, it cannot be turned.
***
**Related Pages:**
+    [Flip proc (icon)](/ref/icon/proc/Flip)
+    [dir](/ref/atom/var/dir)
+    [icon](/ref/icon)
+    [procs (icon)](/ref/icon/proc)
