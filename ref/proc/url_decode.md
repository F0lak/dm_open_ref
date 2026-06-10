
## url_decode (proc)

**Format:**
+   url_decode(UrlText)

**Arguments:**
+   UrlText: text to be "unescaped"

**Returns:**
+   unescaped text
***
Most non-alphanumeric characters are converted to another format in a URL. To send these characters literally, they must be "escaped".

The <code>url_decode()</code> instruction takes a text string containing such escaped symbols and turns them into their literal counterparts. Usually this is done for you automatically in <code>Topic()</code>. The more useful function is <code>url_encode()</code> which does the reverse.
***
**Related Pages:**
+    [Topic proc (client)](/ref/client/proc/Topic)
+    [url_encode proc](/ref/proc/url_encode)
