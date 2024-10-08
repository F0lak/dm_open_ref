## html_decode proc

**Format:**
+   html_decode(HtmlText)

**Args:**
+   HtmlText: text to be "unescaped"

**Returns:**
+   unescaped text

Special characters such as < and > are not displayed
literally in html and may produce garbled output. To display these
characters literally, they must be "escaped". For example, < is
produced by the code `&lt;` and > is produced by the code `&gt;`.

The `html_decode()` instruction takes a text string containing
such escaped symbols and turns them into their literal counterparts. The
more useful function is `html_encode()` which does the reverse.

> [!TIP] 
> **See also:**
> +   [html_encode proc](/ref/proc/html_encode.md) 