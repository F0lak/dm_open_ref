## group var (regex) 
###### BYOND Version 510


After a call to Find(), if this regular expression had any
parentheses groups, whatever text was matched in those groups is stored
here in a list.
### Example

```dm
 var/regex/R = new("B(.)(.)(.)D") R.Find("BYOND") //
find this pattern in "BYOND" 
```
 The result of the example is
that R.group is list("Y","O","N").

> [!TIP] 
> **See also:**
> +   [regex datum](/ref/regex.md) 
> +   [Find proc (regex)](/ref/regex/proc/Find.md) 
> +   [index var (regex)](/ref/regex/var/index.md) 
> +   [match var (regex)](/ref/regex/var/match.md) 