[]{#/browser control (skin).md}/control/browser}    
## browser control (skin)    
A browser panel integrated into the skin.    
**Browser-specific parameters:**    
:   [auto-format](/%7Bskin%7D/param/auto-format)    
:   [on-hide](/%7Bskin%7D/param/on-hide)    
:   [on-show](/%7Bskin%7D/param/on-show)    
:   [show-history](/%7Bskin%7D/param/show-history)    
:   [show-url](/%7Bskin%7D/param/show-url)    
:   [use-title](/%7Bskin%7D/param/use-title)    
Browsers are capable of displaying HTML documents, and can also interact    
with the skin.    
### Browsers and popups    
A longstanding behavior of BYOND is the ability to create a new browser    
window by sending an extra argument to the    
[browse()](/proc/browse){.code} proc. Since the advent of skins in    
BYOND 4.0, this behavior was kept. When you create a new browser popup,    
the window name you specify for the popup is used for the name of a new    
[window control](/%7Bskin%7D/control/main), and within that window    
there will be a new browser control simply called `browser`.    
If you want to interact with the new browser, its full \"decorated\"    
[id](/%7Bskin%7D/param/id){.code} is *`windowname`*`.browser`.    
### Running JavaScript from DM    
Sending [output()](/proc/output){.code} to a browser will send a    
document to display there, but if you follow the browser\'s control name    
with a colon and a function name, you can call a JavaScript function in    
the document displayed within that browser.    
### Example:    
var/list/info = list(\"name\"=\"fridge\", \"power\"=12) // send    
{\"name\":\"fridge\",\"power\":12} to a JavaScript function usr \<\<    
output(url_encode(json_encode(info)), \"mybrowser:myJSfunction\")    
The text that you send as output will be parsed like URL parameters,    
where mutliple arguments to the function are separated by `&` or `;`,    
which is why [url_encode()](/proc/url_encode){.code} is wrapped around    
the [json_encode()](/proc/json_encode){.code} call in this example.    
### More browser options    
These topics cover more advanced uses of the browser control.    
[winset and winget (JavaScript)](/%7Bskin%7D/control/browser/winset)    
:   Interact with the skin via JavaScript    
[byondStorage (browser control)](/%7Bskin%7D/control/browser/byondStorage)    
:   Provides persistent storage options for small data  