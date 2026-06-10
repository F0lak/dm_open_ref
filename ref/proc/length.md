
## length (proc)

**Format:**
+   length(E)

**Arguments:**
+   E: text, list, file, or vector

**Returns:**
+   The length of the data associated with E.
***

```dm

world << length("Hi")

```


This outputs, "2", the length of the string "Hi".


```dm

world << length(list(1,2,3))

```


This outputs, "3", the length of the list.


```dm

world << length(file("test.txt"))

```


This outputs the length of the file.

Note: In strings containing non-ASCII characters, this is the length in bytes, not characters; a character may span multiple bytes. Use `length_char()` to work with character counts instead of bytes. See the <a href="#/{notes}/Unicode">Unicode</a> section for more information.

For vectors, the length is the order of the vector, as in 2 for a 2D vector or 3 for a 3D vector. See <a class="code" href="#/vector/var/len">vector.len</a>.
***
**Related Pages:**
+    [vector](/ref/vector)
