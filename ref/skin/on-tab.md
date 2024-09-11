## on-tab parameter (skin)
**See also:**
*   [current-tab parameter](/ref/%7Bskin%7D/param/current-tab.md) -m
*   [tabs parameter](/ref/%7Bskin%7D/param/tabs.md) -m
<!-- -->
**Applies to:**
*   [Info](/ref/%7Bskin%7D/control/info.md) -m
*   [Tab](/ref/%7Bskin%7D/control/tab.md) -m
<!-- -->
**Format:**
*   string


[Command](/ref/%7Bskin%7D/commands.md) -m executed when the current tab
is changed. 

If you include `[[*]]` in the command, it will be
replaced by the new tab\'s [id](/ref/%7Bskin%7D/param/id.md) -m{.code}. (See
\"Embedded Winget\" in [client commands](/ref/%7Bskin%7D/commands.md) -mfor more
details on the `[[...]]` format.)