## info control (skin)


The classic BYOND statpanel, which contains both stat and verb
tabs. This is technically a 3-column grid with a variable number of
rows.
**Info-specific parameters:**
*   [allow-html](/ref/%7Bskin%7D/param/allow-html.md) -m
*   [highlight-color](/ref/%7Bskin%7D/param/highlight-color.md) -m
*   [multi-line](/ref/%7Bskin%7D/param/multi-line.md) -m
*   [on-hide](/ref/%7Bskin%7D/param/on-hide.md) -m
*   [on-show](/ref/%7Bskin%7D/param/on-show.md) -m
*   [on-tab](/ref/%7Bskin%7D/param/on-tab.md) -m
*   [prefix-color](/ref/%7Bskin%7D/param/prefix-color.md) -m
*   [suffix-color](/ref/%7Bskin%7D/param/suffix-color.md) -m
*   [tab-background-color](/ref/%7Bskin%7D/param/tab-background-color.md) -m
*   [tab-font-family, tab-font-size,
    tab-font-style](/ref/%7Bskin%7D/param/tab-font.md) -m
*   [tab-text-color](/ref/%7Bskin%7D/param/tab-text-color.md) -m


Output to a statpanel is done via the
[stat()](/ref/proc/stat.md) -m{.code} and [statpanel()](/ref/proc/statpanel.md) -m{.code}
procs, during [mob/Stat()](/ref/atom/proc/stat.md) -m{.code}. 

The same
limitations that apply to [grid](/ref/%7Bskin%7D/control/grid.md) -moutput apply
here.