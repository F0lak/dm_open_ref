
## text2num (proc)

**Format:**
+   text2num(T)
+   text2num(T, radix)

**Arguments:**
+   T: A text string.
+   radix: The radix/base of the number, e.g. 16 for hexadecimal

**Returns:**
+   A number.
***
If T is a text string for a number, return the number. Any non-numeric text following the initial portion will be ignored. If there is no initial numeric portion, the result is null.


```dm

var/number = text2num("123")  // = 123

```


The optional radix, which defaults to 10, can be any integer from 2 to 36.
***
**Related Pages:**
+    [istext proc](/ref/proc/istext)
+    [num2text proc](/ref/proc/num2text)
