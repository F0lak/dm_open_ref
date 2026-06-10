
## html_decode (proc)

**Format:**
+   html_decode(HtmlText)

**Arguments:**
+   HtmlText: text to be "unescaped"

**Returns:**
+   unescaped text
***
Special characters such as &lt; and &gt; are not displayed literally in html and may produce garbled output. To display these characters literally, they must be "escaped". For example, &lt; is produced by the code <code>&amp;lt;</code> and &gt; is produced by the code <code>&amp;gt;</code>.

The <code>html_decode()</code> instruction takes a text string containing such escaped symbols and turns them into their literal counterparts. The more useful function is <code>html_encode()</code> which does the reverse.
***
**Related Pages:**
+    [html_encode proc](/ref/proc/html_encode)
