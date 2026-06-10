
## browser (info)
***
A browser panel integrated into the skin.

Browsers are capable of displaying HTML documents, and can also interact with the skin.

A longstanding behavior of BYOND is the ability to create a new browser window by sending an extra argument to the <a class="code" href="#/proc/browse">browse()</a> proc. Since the advent of skins in BYOND 4.0, this behavior was kept. When you create a new browser popup, the window name you specify for the popup is used for the name of a new <a href="#/{skin}/control/main">window control</a>, and within that window there will be a new browser control simply called `browser`.

If you want to interact with the new browser, its full "decorated" <a class="code" href="#/{skin}/param/id">id</a> is `*windowname*.browser`.

Sending <a class="code" href="#/proc/output">output()</a> to a browser will send a document to display there, but if you follow the browser's control name with a colon and a function name, you can call a JavaScript function in the document displayed within that browser.


```dm

var/list/info = list("name"="fridge", "power"=12)
// send {"name":"fridge","power":12} to a JavaScript function
usr << output(url_encode(json_encode(info)), "mybrowser:myJSfunction")

```


The text that you send as output will be parsed like URL parameters, where mutliple arguments to the function are separated by `&amp;` or `;`, which is why <a class="code" href="#/proc/url_encode">url_encode()</a> is wrapped around the <a class="code" href="#/proc/json_encode">json_encode()</a> call in this example.

These topics cover more advanced uses of the browser control.
***