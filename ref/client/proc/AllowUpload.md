## AllowUpload proc (client)

**Format:**
+   AllowUpload(filename, filelength)
<!-- -->
**When:**
+   Called when the player attempts to upload a file to the server,
    through input() or a command.
<!-- -->
**Default action:**
+   Allows the upload by returning 1.


The client who owns this proc (src) is the one trying to upload
the file. If this proc returns a true value, the upload will be allowed.
Otherwise, it will be rejected.
### Example:

``` dm
 client AllowUpload(filename, filelength) if(filelength >=
524288) // 512K (0.5M) src << "[filename] is too big to upload!"
return 0 return 1 
```


> [!TIP] 
> **See also:**
> +   [input proc](/ref/proc/input.md) <!-- -->