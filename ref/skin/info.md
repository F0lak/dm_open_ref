## info control (skin)


The classic BYOND statpanel, which contains both stat and verb
tabs. This is technically a 3-column grid with a variable number of
rows.
**Info-specific parameters:**
+   [allow-html](/ref/skin/param/allow-html.md) 
+   [highlight-color](/ref/skin/param/highlight-color.md) 
+   [multi-line](/ref/skin/param/multi-line.md) 
+   [on-hide](/ref/skin/param/on-hide.md) 
+   [on-show](/ref/skin/param/on-show.md) 
+   [on-tab](/ref/skin/param/on-tab.md) 
+   [prefix-color](/ref/skin/param/prefix-color.md) 
+   [suffix-color](/ref/skin/param/suffix-color.md) 
+   [tab-background-color](/ref/skin/param/tab-background-color.md) 
+   [tab-font-family, tab-font-size,
    tab-font-style](/ref/skin/param/tab-font.md) 
+   [tab-text-color](/ref/skin/param/tab-text-color.md) 


Output to a statpanel is done via the
[stat()](/ref/proc/stat.md)  and [statpanel()](/ref/proc/statpanel.md) 
procs, during [mob/Stat()](/ref/atom/proc/stat.md) . 

The same
limitations that apply to [grid](/ref/skin/control/grid.md) output apply
here.