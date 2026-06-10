
## control (info)
***
Controls can be created or deleted at runtime. (Only controls you created during runtime may be deleted.) To create a control, call <a class="code" href="#/proc/winset">winset()</a> using the <a class="code" href="#/{skin}/param/id">id</a> of the new control, and the parameter list should include <a class="code" href="#/{skin}/param/type">type</a>, <a class="code" href="#/{skin}/param/parent">parent</a>, and probably also <a class="code" href="#/{skin}/param/pos">pos</a>, <a class="code" href="#/{skin}/param/size">size</a>, and any <a href="#/{skin}/param/anchor">anchors</a>.

To delete the control again, set its `parent` to a blank value.

Menu items and macros work similarly, except they have no positional info. For those, the <a class="code" href="#/{skin}/param/name">name</a> parameter is important when you create them, and you will either need <a class="code" href="#/{skin}/param/command">command</a> or (for macros) <a class="code" href="#/{skin}/param/map-to">map-to</a> to do anything with them.
***