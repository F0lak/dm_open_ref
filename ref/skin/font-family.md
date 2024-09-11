## font-family parameter (skin)
**See also:**
*   [font-size parameter](/ref/%7Bskin%7D/param/font-size.md) -m
*   [font-style parameter](/ref/%7Bskin%7D/param/font-style.md) -m
*   [tab-font-family, tab-font-size, tab-font-style
    parameters](/ref/%7Bskin%7D/param/tab-font.md) -m
<!-- -->
**Applies to:**
*   [All](/ref/%7Bskin%7D/control.md) -m<!-- -->
**Format:**
*   string


Leave blank to use the default font. This can be used for
CSS-style fallback fonts, e.g. \"Arial,Helvetica\". 

You can
include fonts in your resource file, making them available to the
client, like so* 
```
 var/list/extra_resources = list(\\
\'myfont.ttf\', \'myfont_bold.ttf\') 
```
