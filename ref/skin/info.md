## info control (skin)


The classic BYOND statpanel, which contains both stat and verb
tabs. This is technically a 3-column grid with a variable number of
rows.
**Info-specific parameters:**
+   [allow-html](/ref/%7Bskin%7D/param/allow-html.md) 
+   [highlight-color](/ref/%7Bskin%7D/param/highlight-color.md) 
+   [multi-line](/ref/%7Bskin%7D/param/multi-line.md) 
+   [on-hide](/ref/%7Bskin%7D/param/on-hide.md) 
+   [on-show](/ref/%7Bskin%7D/param/on-show.md) 
+   [on-tab](/ref/%7Bskin%7D/param/on-tab.md) 
+   [prefix-color](/ref/%7Bskin%7D/param/prefix-color.md) 
+   [suffix-color](/ref/%7Bskin%7D/param/suffix-color.md) 
+   [tab-background-color](/ref/%7Bskin%7D/param/tab-background-color.md) 
+   [tab-font-family, tab-font-size,
    tab-font-style](/ref/%7Bskin%7D/param/tab-font.md) 
+   [tab-text-color](/ref/%7Bskin%7D/param/tab-text-color.md) 


Output to a statpanel is done via the
[stat()](/ref/proc/stat.md)  and [statpanel()](/ref/proc/statpanel.md) 
procs, during [mob/Stat()](/ref/atom/proc/stat.md) . 

The same
limitations that apply to [grid](/ref/%7Bskin%7D/control/grid.md) output apply
here.