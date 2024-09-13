## font-family parameter (skin)

    parameters](/ref/%7Bskin%7D/param/tab-font.md) 
<!-- -->
**Applies to:**
+   [All](/ref/%7Bskin%7D/control.md) <!-- -->
**Format:**
+   string


Leave blank to use the default font. This can be used for
CSS-style fallback fonts, e.g. \"Arial,Helvetica\". 

You can
include fonts in your resource file, making them available to the
client, like so: 
``` dm
 var/list/extra_resources = list(\\
\'myfont.ttf\', \'myfont_bold.ttf\') 
```


> [!TIP] 
> **See also:**
> +   [font-size parameter](/ref/%7Bskin%7D/param/font-size.md) 
> +   [font-style parameter](/ref/%7Bskin%7D/param/font-style.md) 
> +   [tab-font-family, tab-font-size, tab-font-style