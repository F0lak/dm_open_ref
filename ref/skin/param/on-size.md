
## on-size (info)
***
<a href="#/{skin}/commands">Command</a> executed when this control is resized. If you are dragging a window edge or splitter, the command won't run until you finish.

No command will be sent in response to size or splitter changes made by <a class="code" href="#/proc/winset">winset()</a>.

If you include `[[*]]` in the command, it will be replaced by the control's new size. Likewise, `[[width]]` will be replaced with the width and `[[height]]` with the height. (See <a href="#/{skin}/commands/embed">embedded winget</a> for more details on the `[[...]]` format.)
***