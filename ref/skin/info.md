[]{#/{skin}/control/info}    
## info control (skin)    
The classic BYOND statpanel, which contains both stat and verb tabs.    
This is technically a 3-column grid with a variable number of rows.    
**Info-specific parameters:**    
:   [allow-html](/ref/%7Bskin%7D/param/allow-html)    
:   [highlight-color](/ref/%7Bskin%7D/param/highlight-color)    
:   [multi-line](/ref/%7Bskin%7D/param/multi-line)    
:   [on-hide](/ref/%7Bskin%7D/param/on-hide)    
:   [on-show](/ref/%7Bskin%7D/param/on-show)    
:   [on-tab](/ref/%7Bskin%7D/param/on-tab)    
:   [prefix-color](/ref/%7Bskin%7D/param/prefix-color)    
:   [suffix-color](/ref/%7Bskin%7D/param/suffix-color)    
:   [tab-background-color](/ref/%7Bskin%7D/param/tab-background-color)    
:   [tab-font-family, tab-font-size,    
    tab-font-style](/ref/%7Bskin%7D/param/tab-font)    
:   [tab-text-color](/ref/%7Bskin%7D/param/tab-text-color)    
Output to a statpanel is done via the [stat()](/ref/proc/stat){.code} and    
[statpanel()](/ref/proc/statpanel){.code} procs, during    
[mob/Stat()](/ref/atom/proc/stat){.code}.    
The same limitations that apply to [grid](/ref/%7Bskin%7D/control/grid)    
output apply here.  