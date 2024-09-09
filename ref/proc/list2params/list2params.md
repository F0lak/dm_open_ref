[]{#/proc/list2params}    
## list2params proc    
**See also:**    
:   [Topic proc (client)](/ref/client/proc/Topic.md)    
:   [list associations](/ref/list/associations.md)    
:   [params var (world)](/ref/world/var/params.md)    
:   [params2list proc](/ref/proc/params2list.md)    
:   [text2num proc](/ref/proc/text2num.md)    
<!-- -->    
**Format:**    
:   list2params(List)    
<!-- -->    
**Args:**    
:   List: List to encode as a text string.    
This instruction converts a list of parameter names and associated    
values into a single text string suitable for use in a URL or similar    
situation. The format of the resulting text string is:    
\"name1=value1&name2=value2&\...\"    
Special characters such as \'=\' and \'&\' inside the parameter names or    
values are written in the form: `%xx` where `xx` are two hexadecimal    
digits representing the ASCII value of the character. For    
[Unicode](/ref/%7Bnotes%7D/Unicode.md) characters, their UTF-8 encoding will    
be processed this way, which may make up multiple `%xx` sequences. In    
addition, spaces are converted to `+`.    
This parameter format is the same one used by most HTML forms and is    
known by the MIME type `application/x-www-form-urlencoded`. It is often    
used in DM to pack information into topic links.    
The original list has items `"name1"`, `"name2"`, and so on. These in    
turn are associated with the corresponding values `"value1"`,    
`"value2"`, and so on.    
### Example:    
var/plist\[0\] plist\[\"offense\"\] = \"jwalk\" plist\[\"time\"\] =    
\"10:00\" usr \<\< list2params(plist)    
The above example creates a simple parameter list which associates the    
item \"offense\" with the value \"jwalk\" and the item \"time\" with the    
value \"10:00\". This will produce the text string    
\"offense=jwalk&time=10:00\".    
Object values in the list (like say a mob) get turned into references in    
the parameter text, just as though you had embedded them with    
\"\\ref\[Object\]\". When read back in with params2list(), you could    
convert these values back into real references by using locate().  