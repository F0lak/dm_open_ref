
## font-family (info)
***
Leave blank to use the default font. This can be used for CSS-style fallback fonts, e.g. "Arial,Helvetica".

You can include fonts in your resource file, making them available to the client, like so:


```dm

var/list/extra_resources = list(\
    'myfont.ttf',
    'myfont_bold.ttf')

```

***