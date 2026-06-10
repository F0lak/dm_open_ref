
## tabs (info)
***
A comma-separated list of <a class="code" href="#/{skin}/param/id">id</a> values for the panes included as tabs in this control.

When setting this value, you can put `+` in front of the list to add tabs to the existing control, without affecting current tabs. You can likewise use `-` in front of the list to remove tabs.

Note: When using this with <a class="code" href="#/proc/winset">winset()</a>, remember you will need to escape `+` as `%2B` via <a class="code" href="#/proc/url_encode">url_encode()</a> or <a class="code" href="#/proc/list2params">list2params()</a>.
***