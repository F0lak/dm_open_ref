## on-tab parameter (skin)

<!-- -->
**Applies to:**
+   [Info](/ref/%7Bskin%7D/control/info.md) 
+   [Tab](/ref/%7Bskin%7D/control/tab.md) 
<!-- -->
**Format:**
+   string


[Command](/ref/%7Bskin%7D/commands.md)  executed when the current tab
is changed. 

If you include `[[*]]` in the command, it will be
replaced by the new tab\'s [id](/ref/%7Bskin%7D/param/id.md) . (See
\"Embedded Winget\" in [client commands](/ref/%7Bskin%7D/commands.md) for more
details on the `[[...]]` format.)

> [!TIP] 
> **See also:**
> +   [current-tab parameter](/ref/%7Bskin%7D/param/current-tab.md) 
> +   [tabs parameter](/ref/%7Bskin%7D/param/tabs.md) 