## sha1 proc 
###### BYOND Version 513

<!-- -->
**Format:**
+   sha1(T)
+   sha1(F)
<!-- -->
**Returns:**
+   text or null.
<!-- -->
**Args:**
+   T: A text string.
+   F: A file.


This proc implements SHA1 hashing. A hash function is a one-way
process that compacts information to a short value: a hash. The same
value will always have the same hash. Among other uses, most computers
use hashing to store passwords. By storing just the hash, the password
file contains very little sensitive information, but the password can
still be verified by confirming that `sha1(password)==hash`. SHA1 is a
widely-used hash function.
### Example:

```
 mob/var/hash mob/Read(savefile/S) ..() // hash was saved in
the file along with other values
if(sha1(\"\[level\]/\[exp\]/\[exp_needed\]\") != hash) src \<\<
\"Cheater!\" del(src) 
```
 

In the example, a few vars
belonging to a mob were saved along with a hash of those values. When
the mob is loaded again, the game compares the hash to the values to
make sure it\'s still accurate. If the values or hash had been changed
by a sneaky player, they wouldn\'t match. (But a sneaky player could
still calculate `hash` themselves if they knew the exact text used to
make it, so this should be kept secret.) 

If the argument is a
file, `sha1()` will read the file and return the SHA1 hash of the
file\'s entire contents. If the file doesn\'t exist, it returns null.
The file may be a cache file or an external file.
### Examples:

```
 var/hash = \"(insert hash value here)\" // Compute this ahead
of time // Check that the cached default icon is still the same if
(sha1(\'default.dmi\') != hash) world \<\< \"The default icon has been
modified!\" // Or check that the entire game resource file is pristine
if (sha1(file(\"mygame.rsc\")) != hash) world \<\< \"The game resources
have been modified!\" 
```
 

Note that you must pass the
result of [file()](/ref/proc/file.md) in order to compute the hash of
an external file\'s contents at runtime. Otherwise `sha1()` will treat
the filename as text and return the hash of the name only. 

If
`T` is anything but a text string or file, the proc returns null.

> [!TIP] 
> **See also:**
> +   [md5 proc](/ref/proc/md5.md) 
> +   [file proc](/ref/proc/file.md) 