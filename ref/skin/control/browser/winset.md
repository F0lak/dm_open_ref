
## winset (info)
***
Browser controls can interact with the skin via JavaScript, by setting `window.location` to a special URL.

This works like an ordinary <a class="code" href="#/proc/winset">winset()</a> call from the server. If `id` is omitted, it's the same as a winset with a null ID. You can also leave the `id` blank if you use "fully decorated" property names such as `mybutton.is-checked` instead of just `is-checked`.

Any text you use other than letters, numbers, hyphens, commas, and periods should be encoded via the `encodeURIComponent()` function in JavaScript.

In this winget, the IDs and properties you want can be separated by commas if you want to retrieve more than one. The winget operation works via a callback function you must define in JavaScript. The callback is given just one argument, a JavaScript object with all of the properties you requested. For example, this URL:

...might send this to the callback function `wgcb`:

The property names will be in the same format you would expect from <a class="code" href="#/proc/winget">winget()</a>, so when you're looking at multiple elements' properties, you'll get the full names in `id.property` format. The values are always sent back in a convenient form for JavaScript to work with; in the case of size, position, and color these will always be objects.

An optional `control` parameter for the winget call can be used if you want to send data to a callback in a different browser control.
***