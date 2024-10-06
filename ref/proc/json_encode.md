## json_encode proc 
###### BYOND Version 510

**Format:**
+   json_encode(Value)
+   json_encode(Value, flags)
<!-- -->
**Returns:**
+   A JSON-formatted text string representing Value.
<!-- -->
**Args:**
+   Value: The value to encode.
+   flags: A set of flags that tell the encoder how to act.


If Value is a simple list or a matrix, the result will be
formatted as a JSON array, and each item in the list is encoded.


If Value is an associative list, the result will be formatted
as a JSON object literal, and each item and associated value is encoded.
(The keys in the object literal don\'t have to be strings. Even though
that isn\'t valid JSON, BYOND doesn\'t care. Be aware however that
strict JSON parsers *will* care.) 

Datums are *not* serialized,
but are converted to the equivalent of `"[Value]"` instead. 

The
special numbers NaN and infinity will be encoded as object literals in a
form like `{"__number__":"NaN"}`.
### Example:

```dm
 var/list/info = list("name"="fridge", "power"=12) //
send {"name":"fridge","power":12} to a JavaScript function usr
<< output(url_encode(json_encode(info)), "mybrowser:myJSfunction")

```
 

BYOND formatting such as \\red is removed from
encoded strings. 

Situations where a list has a reference to
itself will cause the nested version to print a null value instead.


The `JSON_PRETTY_PRINT` flag introduces spacing into the output
for improved readibility. Spaces will be added after colons and commas.
Non-empty arrays and object literals will have a line break and tabs
before each item, and a line break with one fewer tab before the closing
bracket or brace. (The special formatting for numbers like Infinity, or
the list form for matrices, will not be given tabs and line breaks.)

> [!TIP] 
> **See also:**
> +   [json_decode proc](/ref/proc/json_decode.md) <!-- -->