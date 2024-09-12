## tabs parameter (skin)

<!-- -->
**Applies to:**
+   [Tab](/ref/%7Bskin%7D/control/tab.md) 
<!-- -->
**Format:**
+   string


A comma-separated list of [id](/ref/%7Bskin%7D/param/id.md) {.code}
values for the panes included as tabs in this control. 

When
setting this value, you can put `+` in front of the list to add tabs to
the existing control, without affecting current tabs. You can likewise
use `-` in front of the list to remove tabs. 

Note: When using
this with [winset()](/ref/proc/winset.md) {.code}, remember you will need to
escape `+` as `%2B` via [url_encode()](/ref/proc/url_encode.md) {.code} or
[list2params()](/ref/proc/list2params.md).

**See also:**
+   [current-tab parameter](/ref/%7Bskin%7D/param/current-tab.md) 
+   [id parameter](/ref/%7Bskin%7D/param/id.md) 
+   [multi-line parameter](/ref/%7Bskin%7D/param/multi-line.md) 