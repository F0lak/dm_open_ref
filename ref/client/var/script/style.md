
## style (var)
***
Style sheets may be included in DM Script by putting the style sheet inside the HTML tags <code>&lt;STYLE&gt;</code> and <code>&lt;/STYLE&gt;</code>. In general, any text enclosed in start and end tags will be sent to the player's terminal, so you could use <code>client.script</code> to output a welcome message as well as loading a style sheet.


```dm

client/script = ""

```


This example style sheet makes the player's terminal have a black background and aqua colored text. When changing the background color, it is important to change the color of system and link text as well. See the section on <a href="#/DM/text/style">style sheets</a> for an example.
***
**Related Pages:**
+    [script var (client)](/ref/client/var/script)
+    [style sheets](/ref/DM/text/style)
