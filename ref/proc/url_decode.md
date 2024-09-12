## url_decode proc

**Format:**
+   url_decode(UrlText)
<!-- -->
**Args:**
+   UrlText: text to be \"unescaped\"
<!-- -->
**Returns:**
+   unescaped text


Most non-alphanumeric characters are converted to another
format in a URL. To send these characters literally, they must be
\"escaped\". 

The `url_decode()` instruction takes a text string
containing such escaped symbols and turns them into their literal
counterparts. Usually this is done for you automatically in `Topic()`.
The more useful function is `url_encode()` which does the reverse.

**See also:**
+   [Topic proc (client)](/ref/client/proc/Topic.md) 
+   [url_encode proc](/ref/proc/url_encode.md) <!-- -->