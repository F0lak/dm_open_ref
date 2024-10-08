## on-tab parameter (skin)


**Applies to:**
+   [Info](/ref/skin/control/info.md) 
+   [Tab](/ref/skin/control/tab.md) 

**Format:**
+   string


[Command](/ref/skin/commands.md)  executed when the current tab
is changed. 

If you include `[[*]]` in the command, it will be
replaced by the new tab\'s [id](/ref/skin/param/id.md) . (See
"Embedded Winget" in [client commands](/ref/skin/commands.md) for more
details on the `[[...]]` format.)

> [!TIP] 
> **See also:**
> +   [current-tab parameter](/ref/skin/param/current-tab.md) 
> +   [tabs parameter](/ref/skin/param/tabs.md) 