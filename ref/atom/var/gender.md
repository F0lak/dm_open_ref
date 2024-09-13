## gender var (atom)

**Default value:**
+   \"neuter\"


This sets the object\'s gender. This influences text macros
like `\he`, which may expand to \"it\", \"he\", \"she\", or \"they\".
Valid values are: 
``` dm
 \"neuter\" \"male\" \"female\"
\"plural\" 
```
 These are also defined as constants, which may
help prevent typos, since the compiler will complain if it doesn\'t
recognize what you type: 
``` dm
 NEUTER MALE FEMALE PLURAL

```


> [!TIP] 
> **See also:**
> +   [macros (text)](/ref/DM/text/macros.md) 
> +   [name var (atom)](/ref/atom/var/name.md) <!-- -->