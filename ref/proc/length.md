## length proc

<!-- -->
**Format:**
+   length(E)
<!-- -->
**Returns:**
+   The length of the data associated with E.
<!-- -->
**Args:**
+   E: text, list, file, or vector
### Example:

```dm
 world << length("Hi") 
```
 

This
outputs, "2", the length of the string "Hi".
### Example:

```dm
 world << length(list(1,2,3)) 
```
 

This
outputs, "3", the length of the list.
### Example:

```dm
 world << length(file("test.txt")) 
```



This outputs the length of the file. 

Note: In strings
containing non-ASCII characters, this is the length in bytes, not
characters; a character may span multiple bytes. Use `length_char()` to
work with character counts instead of bytes. See the
[Unicode](/ref/notes/Unicode.md)  section for more information.


For vectors, the length is the magnitude of the vector. See
[vector.len](/ref/vector/var/len.md).

> [!TIP] 
> **See also:**
> +   [vector](/ref/vector.md) 