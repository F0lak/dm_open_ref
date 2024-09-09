[]{#/{skin}/control/info}    
## info control (skin)    
The classic BYOND statpanel, which contains both stat and verb tabs.    
This is technically a 3-column grid with a variable number of rows.    
**Info-specific parameters:**    
:   [allow-html](/ref/%7Bskin%7D/param/allow-html/allow-html.md)    
:   [highlight-color](/ref/%7Bskin%7D/param/highlight-color/highlight-color.md)    
:   [multi-line](/ref/%7Bskin%7D/param/multi-line/multi-line.md)    
:   [on-hide](/ref/%7Bskin%7D/param/on-hide/on-hide.md)    
:   [on-show](/ref/%7Bskin%7D/param/on-show/on-show.md)    
:   [on-tab](/ref/%7Bskin%7D/param/on-tab/on-tab.md)    
:   [prefix-color](/ref/%7Bskin%7D/param/prefix-color/prefix-color.md)    
:   [suffix-color](/ref/%7Bskin%7D/param/suffix-color/suffix-color.md)    
:   [tab-background-color](/ref/%7Bskin%7D/param/tab-background-color/tab-background-color.md)    
:   [tab-font-family, tab-font-size,    
    tab-font-style](/ref/%7Bskin%7D/param/tab-font/tab-font.md)    
:   [tab-text-color](/ref/%7Bskin%7D/param/tab-text-color/tab-text-color.md)    
Output to a statpanel is done via the [stat()](/ref/proc/stat/stat.md){.code} and    
[statpanel()](/ref/proc/statpanel/statpanel.md){.code} procs, during    
[mob/Stat()](/ref/atom/proc/stat/stat.md){.code}.    
The same limitations that apply to [grid](/ref/%7Bskin%7D/control/grid/grid.md)    
output apply here.  