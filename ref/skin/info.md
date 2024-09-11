## info control (skin)


The classic BYOND statpanel, which contains both stat and verb
tabs. This is technically a 3-column grid with a variable number of
rows.
**Info-specific parameters:**
*   [allow-html](/%7Bskin%7D/param/allow-html)
*   [highlight-color](/%7Bskin%7D/param/highlight-color)
*   [multi-line](/%7Bskin%7D/param/multi-line)
*   [on-hide](/%7Bskin%7D/param/on-hide)
*   [on-show](/%7Bskin%7D/param/on-show)
*   [on-tab](/%7Bskin%7D/param/on-tab)
*   [prefix-color](/%7Bskin%7D/param/prefix-color)
*   [suffix-color](/%7Bskin%7D/param/suffix-color)
*   [tab-background-color](/%7Bskin%7D/param/tab-background-color)
*   [tab-font-family, tab-font-size,
    tab-font-style](/%7Bskin%7D/param/tab-font)
*   [tab-text-color](/%7Bskin%7D/param/tab-text-color)


Output to a statpanel is done via the
[`stat()`](/proc/stat) and [`statpanel()`](/proc/statpanel)
procs, during [`mob/Stat()`](/atom/proc/stat). 

The same
limitations that apply to [grid](/%7Bskin%7D/control/grid) output apply
here.