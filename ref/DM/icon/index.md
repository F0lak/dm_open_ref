
## icon (info)
***
An icon file may be referenced by putting single quotes around the filename. The file extension determines the type of icon. Currently supported icon types are <code>.dmi</code>, <code>.bmp</code>, <code>.png</code>, <code>.jpg</code>, and <code>.gif</code>. To create dmi icons, use the Dream Maker icon editor. This allows you to make animations, 4 or 8 directional icons, and icons with different states (such as "live" and "dead").


```dm

  mob
    icon = 'monster.dmi'

```


You can also load icons into memory at run-time and manipulate the graphical data to produce new icons dynamically. This is done by creating an <a href="#/icon">/icon</a> object.
***
**Related Pages:**
+    [FILE_DIR definition](/ref/DM/preprocessor/define/FILE_DIR)
+    [cache](/ref/DM/cache)
+    [flick proc](/ref/proc/flick)
+    [icon](/ref/icon)
+    [icon var (atom)](/ref/atom/var/icon)
+    [icon_state](/ref/atom/var/icon_state)
+    [image objects](/ref/image)
