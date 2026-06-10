
## tags (info)
***
Text tags (also known as <em>elements</em> by snooty HTML purists) control how the text is formatted. HTML syntax is used, so all tags start with <code>&lt;</code> and end with <code>&gt;</code>. The tags which are currently supported by Dream Seeker, are listed below:

In addition to these, the <code>&lt;BEEP&gt;</code> tag, which is not standard HTML, may be used to beep the terminal.

Some tags take additional parameters, known as attributes. The most common ones are <code>&lt;FONT&gt;</code> and <code>&lt;A&gt;</code>. The syntax for these is illustrated by the following two examples:


```dm

"How about this!"
"Click here!"

```


As many attributes may be specified as desired. The attribute value may have quotes around it, but this is only necessary if the value contains spaces. It is usually more convenient to use single quotes so you don't have to escape the double quotes, but you can also embed the HTML in a <a href="#/DM/text">text document</a> to avoid the need for escaping quotes.

When applying color to text, you can use hexadecimal RGB or you can use one of the named <a href="#/{{appendix}}/html-colors">HTML colors</a>.

Text sizes range from 1 to 7, 1 being the smallest and 7 being the largest. In addition to absolute sizes, relative sizes may be specified (like +1 for one size bigger or -1 for one size smaller).
***
**Related Pages:**
+    [entities (text)](/ref/DM/text/entities)
+    [macros (text)](/ref/DM/text/macros)
+    [style sheets](/ref/DM/text/style)
+    [text](/ref/DM/text)
