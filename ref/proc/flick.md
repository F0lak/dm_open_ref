
## flick (proc)

**Format:**
+   flick(Icon,Object)

**Arguments:**
+   Icon:  An icon file or state name.
+   Object:   The target object.
***
Cause the icon attached to Object to be temporarily replaced with the specified icon or icon state for the duration of the animation. This is a purely visual effect and does not effect the actual value of the object's icon variable.


```dm

flick('blink.dmi',usr) //show another icon
flick("fight",usr)     //show usr's fight state

```


The target object may be any atom or image.
***
**Related Pages:**
+    [icon_state](/ref/atom/var/icon_state)
