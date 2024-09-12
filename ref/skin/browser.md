## browser control (skin)


A browser panel integrated into the skin.
**Browser-specific parameters:**
+   [auto-format](/ref/%7Bskin%7D/param/auto-format.md) 
+   [on-hide](/ref/%7Bskin%7D/param/on-hide.md) 
+   [on-show](/ref/%7Bskin%7D/param/on-show.md) 
+   [show-history](/ref/%7Bskin%7D/param/show-history.md) 
+   [show-url](/ref/%7Bskin%7D/param/show-url.md) 
+   [use-title](/ref/%7Bskin%7D/param/use-title.md) 


Browsers are capable of displaying HTML documents, and can also
interact with the skin.
### Browsers and popups


A longstanding behavior of BYOND is the ability to create a new
browser window by sending an extra argument to the
[browse()](/ref/proc/browse.md) {.code} proc. Since the advent of skins in
BYOND 4.0, this behavior was kept. When you create a new browser popup,
the window name you specify for the popup is used for the name of a new
[window control](/ref/%7Bskin%7D/control/main.md) , and within that window
there will be a new browser control simply called `browser`. 

If
you want to interact with the new browser, its full \"decorated\"
[id](/ref/%7Bskin%7D/param/id.md) {.code} is *`windowname`*`.browser`.
### Running JavaScript from DM


Sending [output()](/ref/proc/output.md) {.code} to a browser will send
a document to display there, but if you follow the browser\'s control
name with a colon and a function name, you can call a JavaScript
function in the document displayed within that browser.
### Example:

```
 var/list/info = list(\"name\"=\"fridge\", \"power\"=12) //
send {\"name\":\"fridge\",\"power\":12} to a JavaScript function usr
\<\< output(url_encode(json_encode(info)), \"mybrowser:myJSfunction\")

```
 

The text that you send as output will be parsed like
URL parameters, where mutliple arguments to the function are separated
by `&` or `;`, which is why [url_encode()](/ref/proc/url_encode.md) {.code} is
wrapped around the [json_encode()](/ref/proc/json_encode.md) {.code} call in
this example.
### More browser options


These topics cover more advanced uses of the browser control.
[winset and winget (JavaScript)](/ref/%7Bskin%7D/control/browser/winset.md) 
+   Interact with the skin via JavaScript
[byondStorage (browser control)](/ref/%7Bskin%7D/control/browser/byondStorage.md) :   Provides persistent storage options for small data