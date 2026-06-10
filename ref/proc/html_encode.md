
## html_encode (proc)

**Format:**
+   html_encode(PlainText)

**Arguments:**
+   PlainText: text to be html "escaped"

**Returns:**
+   escaped text
***
Special characters such as &lt; and &gt; are not displayed literally in html and may produce garbled output. If you want to ensure that an entire text string is displayed literally, you can "escape" those characters. For example, &lt; is produced by the code <code>&amp;lt;</code> and &gt; is produced by the code <code>&amp;gt;</code>.

The <code>html_encode()</code> instruction does this for you automatically. If you wanted to disallow html input from players, you could use this to force their text to be displayed literally:


```dm

mob/verb/say(T as text)
   view() << "[usr] says, '[html_encode(T)]'"

```


If a URL is included in the text, special characters like &amp; that are part of the URL will be skipped. This keeps automatically created links in the output from being broken.

Note for BYOND oldies: the old-style formatting codes such as "\red" which are still parsed but not encouraged are completely stripped out by html_encode().
***
**Related Pages:**
+    [html_decode proc](/ref/proc/html_decode)
