
## AllowUpload (proc)

**Format:**
+   AllowUpload(filename, filelength)

**Called When:**
+   Called when the player attempts to upload a file to the server, through input() or a command.

**Default Action:**
+   Allows the upload by returning 1.
***
The client who owns this proc (src) is the one trying to upload the file. If this proc returns a true value, the upload will be allowed. Otherwise, it will be rejected.


```dm

client
   AllowUpload(filename, filelength)
      if(filelength >= 524288)  // 512K (0.5M)
         src << "[filename] is too big to upload!"
         return 0
      return 1

```

***
**Related Pages:**
+    [input proc](/ref/proc/input)
