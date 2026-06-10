
## icon (info)
***
An `/icon` object is created by loading an icon file into memory for direct access and manipulation. In order to be displayed, an `/icon` object always gets converted back into an icon file; this happens automatically when you assign atom.icon to an `/icon` object, since that variable may only refer to a static icon file, rather than a dynamic memory object.

To create an `/icon` object, simply use `new/icon()`, or the short-cut `icon()` proc. The following example loads an icon file, reddens it, and then assigns it back to the player's icon, which implicitly creates a new icon file.


```dm

mob/verb/test()
   var/icon/I = new('player.dmi')
   I.Blend(rgb(40,0,0))
   usr.icon = I

```


Note that merely displaying different icon states or directions can generally be achieved without any icon manipulation, which saves quite a bit of overhead. For example, the variables `atom.icon_state` and `atom.dir` can be used to control how `atom.icon` is displayed, without any need for generating a new icon file.

Many things that used to require icon manipulation may not need you to do so anymore, as DM has evolved new capabilities.
***
**Related Pages:**
+    [procs (icon)](/ref/icon/proc)
+    [icons](/ref/DM/icon)
+    [image objects](/ref/image)
+    [stddef.dm file](/ref/{{appendix}}/stddef%2edm)
