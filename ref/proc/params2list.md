
## params2list (proc)

**Format:**
+   params2list(Params)

**Arguments:**
+   Params: Text string of parameter values.

**Returns:**
+   An associative list of parameter names and values.
***
This instruction converts a parameter text string to a list of individual parameters and associated values. The format of the parameter text is:


```dm

"name1=value1&name2=value2&..."

```


The field separator `;` may be used in place of `&amp;`.

Special characters such as `=`, `;`, and `&amp;` inside the parameter names or values should be written in the form <code>%xx</code>, where <code>xx</code> are two hexadecimal digits representing the ASCII value of the character. (For <a href="#/{notes}/Unicode">Unicode</a> characters, this may be several <code>%xx</code> sequences using UTF-8 encoding.) For example, `=` would be written <code>%3d</code>, `;` would be <code>%3b</code>, `&amp;` would be <code>%26</code>, and `%` would be <code>%25</code>. These "escaped" codes are automatically translated into the corresponding character when read by `params2list()`.

This parameter format is the same one used by most HTML forms and is known by the MIME type `application/x-www-form-urlencoded`. It is often used in DM to pack information into topic links. Though DM does not require it, the standard format is for newlines to be written as CR LF pairs (<code>%0d%0a</code>) and spaces to be written as `+` characters. That means if you want to write a `+` symbol, you will have to use <code>%2b</code>.

The list produced from the parameter text has items `"name1"`, `"name2"`, and so on. To access the values associated with these, you use the parameter name as the list index.


```dm

var/ptext = "offense=jwalk&time=10:00"
var/plist[] = params2list(ptext)

var/p
for(p in plist)
   usr << "[p] = [plist[p]]"

```


The above example defines a simple parameter text string containing two parameters: `"offense"` and `"time"`. These are associated with the values `"jwalk"` and `"10:00"`. The <code>for</code> loop illustrates how one might loop through the list and print out each setting.

Note that all values are stored as text strings in the list. If you wish to perform a numerical operation (such as addition), you should convert the value to a number first using `text2num()`. If the value is an object text reference, you can convert that into the object itself by using `locate()`.

If you have multiple items with the same name, they will be combined into a list of text strings. For example, `"key=value1;key=value2"` would set `list["key"]` to a list containing `"value1"` and `"value2"`, not necessarily in that order.
***
**Related Pages:**
+    [Topic proc (client)](/ref/client/proc/Topic)
+    [list associations](/ref/list/associations)
+    [list2params](/ref/proc/list2params)
+    [params](/ref/world/var/params)
+    [text2num proc](/ref/proc/text2num)
